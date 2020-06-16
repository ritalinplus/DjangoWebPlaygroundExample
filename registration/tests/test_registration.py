from django.test import TestCase
from django.contrib.auth.models import User

from registration.models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        # Creates a password and encrypt it.
        User.objects.create_user('test', 'test@test.com', 'test1234')

    def test_profile_exists(self):
        exists = Profile.objects.filter(user__username='test').exists()
        self.assertTrue(exists)
