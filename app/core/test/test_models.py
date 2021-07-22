from django.test import TestCase
from django.contrib.auth import get_user_model

class ModalTests(TestCase):
    def test_create_user_with_email(self):
        """Creating a new user with email is success"""
        email = "sanjana.maheshwari456@gmail.com"
        password = "test"
        user = get_user_model().objects.create_user(
            email = email,
            password = password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
