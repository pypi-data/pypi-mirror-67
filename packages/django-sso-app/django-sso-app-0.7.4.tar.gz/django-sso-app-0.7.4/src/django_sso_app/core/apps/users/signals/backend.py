import logging

from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver

logger = logging.getLogger('django_sso_app.core.apps.users.signals')


@receiver(user_logged_in)
def post_user_login(**kwargs):
    user = kwargs['user']

    logger.debug('Users, "{}" LOGGED IN!!!'.format(user))
