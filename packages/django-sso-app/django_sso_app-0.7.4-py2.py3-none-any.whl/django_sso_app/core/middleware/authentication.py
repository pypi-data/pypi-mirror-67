import logging
# import inspect

from jwt.exceptions import InvalidSignatureError

from django.contrib import auth
from django.core.exceptions import ImproperlyConfigured
from django.utils.deprecation import \
    MiddlewareMixin  # https://stackoverflow.com/questions/42232606/django
# -exception-middleware-typeerror-object-takes-no-parameters
from django.utils.encoding import smart_str
from django.conf import settings

from ..tokens.utils import get_request_jwt, jwt_decode
from ..permissions import is_authenticated, is_django_staff
from ..exceptions import ServiceSubscriptionRequiredException, RequestHasValidJwtWithNoDeviceAssociated
from ..utils import check_user_can_login  # , set_session_key
from ..apps.api_gateway.functions import get_apigateway_sso_id
from ... import app_settings

logger = logging.getLogger('django_sso_app.core.middleware')

ADMIN_URL = '/{}'.format(settings.ADMIN_URL)
SSO_ID_JWT_KEY = 'sso_id'


class DjangoSsoAppAuthenticationMiddleware(MiddlewareMixin):
    """
    See django.contrib.auth.middleware.RemoteUserMiddleware.
    """

    # Name of request header to grab username from.  This will be the key as
    # used in the request.META dictionary, i.e. the normalization of headers to
    # all uppercase and the addition of "HTTP_" prefix apply.
    header = app_settings.APIGATEWAY_CONSUMER_USERNAME_HEADER
    # Username for anonymous user
    anonymous_username = app_settings.APIGATEWAY_ANONYMOUS_CONSUMER_USERNAME

    # request info
    request_method = None
    request_path = None
    request_id = None
    request_ip = None

    @staticmethod
    def _remove_invalid_user(request):
        """
        Removes the current authenticated user in the request which is invalid.
        """
        logger.info('removing invalid user "{}"'.format(request.user))
        auth.logout(request)

    def process_request(self, request):

        # AuthenticationMiddleware is required so that request.user exists.
        if not hasattr(request, 'user'):
            raise ImproperlyConfigured(
                "SSO middleware requires the authentication middleware to be"
                " installed.  Edit your MIDDLEWARE setting to insert"
                " 'django.contrib.auth.middleware.AuthenticationMiddleware'"
                " before the SsoMiddleware class.")


        # saving request info
        self.request_method = request.method
        self.request_path = request.path
        self.request_id = id(request)
        self.request_ip = request.META.get('REMOTE_ADDR', None)

        logger.info('--- "{}" request "{}" path "{}" method "{}"'.format(self.request_ip,
                                                                         self.request_id,
                                                                         self.request_path,
                                                                         self.request_method))

        # requesting user
        request_user = request.user


        # skipping django staff users
        if is_django_staff(request_user):
            logger.info('Skipping django staff user "{}"'.format(request_user))
            #  >= 1.10 has is_authenticated as parameter
            # If a staff user is already authenticated, we don't need to
            # continue
            # set_session_key(request, '__dssoa__user', request_user)
            return


        if self.request_path.startswith(ADMIN_URL):
            #  >= 1.10 has is_authenticated as parameter
            # If a staff user is already authenticated, we don't need to
            # continue
            if is_authenticated(request_user):
                _msg = 'Non staff user "{}" tried to enter admin path'.format(request_user)
                logger.warning(_msg)

                self._remove_invalid_user(request)
            else:
                logger.info('Skipping admin path')

            return

        """
        if self.request_path.startswith('/api/v1/passepartout'):
            logger.info('is passepartout path')
            # set_session_key(request, '__dssoa__is_passepartout_path', True)
        """

        consumer_username = None
        request_jwt = None
        verify_jwt = True

        if app_settings.APIGATEWAY_ENABLED:
            # getting sso_id by apigateway consumer username
            try:
                consumer_username = request.META[self.header]

                if consumer_username == self.anonymous_username:
                    if is_authenticated(request_user):
                        logger.info('consumer is anonymous, returning')
                        self._remove_invalid_user(request)
                    return

            except KeyError as e:
                # If specified header or jwt doesn't exist then remove any existing
                # authenticated user, or return (leaving request.user set to
                # AnonymousUser by the AuthenticationMiddleware).
                if is_authenticated(request_user):
                    logger.info('authentication middleware KeyError "{}"'.format(e))
                    self._remove_invalid_user(request)
                return

            else:
                sso_id = get_apigateway_sso_id(consumer_username)


        # validating request jwt

        try:
            request_jwt = get_request_jwt(request, encoded=False)

            if request_jwt is None:
                # If request has no JWT authentication skips
                logger.info('No JWT in request, skipping')
                return
            else:
                # decoding request JWT
                request_device, decoded_jwt = jwt_decode(request_jwt, verify=verify_jwt)

        except KeyError:
            logger.warning('Error decoding JWT "{}"'.format(request_jwt))

            if is_authenticated(request_user):
                self._remove_invalid_user(request)
            return

        except InvalidSignatureError:
            logger.warning('Invalid JWT signature "{}"'.format(request_jwt))

            if is_authenticated(request_user):
                self._remove_invalid_user(request)
            return

        else:
            if decoded_jwt is None:
                logger.warning('No decoded JWT for "{}"'.format(request_jwt))
            else:
                sso_id = decoded_jwt[SSO_ID_JWT_KEY]


        # If the user is already authenticated and that user is active and the
        # one we are getting passed in the headers, then the correct user is
        # already persisted in the session and we don't need to continue.

        # double check sso_id equality between received jwt and sso_app_profile
        if is_authenticated(request_user):
            # check declared sso_id
            if smart_str(request_user.sso_id) == sso_id:
                logger.debug('user is ok')
                #set_session_key(request, '__dssoa__user', request_user)
                return
            else:
                # An authenticated user is associated with the request, but
                # it does not match the authorized user in the header.
                logger.warning('sso_id differs! "{}" "{}"'.format(sso_id, request_user.sso_id))
                self._remove_invalid_user(request)
                return


        # We are seeing this user for the first time in this session, attempt
        # to authenticate the user.
        try:
            if app_settings.APIGATEWAY_ENABLED:
                user = auth.authenticate(request=request,
                                         consumer_username=consumer_username,
                                         encoded_jwt=request_jwt,
                                         decoded_jwt=decoded_jwt)
            else:
                user = auth.authenticate(request=request,
                                         encoded_jwt=request_jwt,
                                         decoded_jwt=decoded_jwt)

        except ServiceSubscriptionRequiredException as e:
            logger.info('ServiceSubscriptionRequiredException')
            if is_authenticated(request_user) and app_settings.APP_ENABLED:
                self._remove_invalid_user(request)

            return e.response

        except RequestHasValidJwtWithNoDeviceAssociated:
            logger.exception('RequestHasValidJwtWithNoDeviceAssociated')

            if is_authenticated(request_user):
                self._remove_invalid_user(request)

            return

        except Exception as e:
            logger.exception('generic middleware exception "{}"'.format(e))
            if is_authenticated(request_user):
                self._remove_invalid_user(request)
            return

        # finishing

        if user is not None:
            # User is valid.  Set request.user and persist user in the session
            # by logging the user in.

            try:
                check_user_can_login(user)

            except Exception as e:
                logger.exception('Authentication middleware check_user_can_login exception "{}"'.format(e))

                if is_authenticated(request_user):
                    self._remove_invalid_user(request)

                return

            else:
                logger.info('User "{}" authenticated successfully!'.format(user))

                # set request user
                setattr(request, 'user', user)  # !!

    def process_response(self, request, response):
        logger.info('--- "{}" response "{}" path "{}" method "{}" ({})'.format(self.request_ip,
                                                                               self.request_id,
                                                                               self.request_path,
                                                                               self.request_method,
                                                                               response.status_code))

        return response
