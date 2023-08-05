# profile filed update updates rev

from django.contrib.auth import get_user_model

from django_sso_app.backend.tests.factories import UserTestCase

User = get_user_model()


class UserModelTestCase(UserTestCase):

    def test_django_superuser_user_creation_creates_sso_app_profile_with_sso_id_equals_to_username(self):
        self.assertEqual(self.admin_user.sso_id, self.admin_user.username)

    def test_django_staff_user_creation_creates_sso_app_profile_with_sso_id_equals_to_username(self):
        self.assertEqual(self.staff_user.sso_id, self.staff_user.username)
