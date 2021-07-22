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

    def test_create_user_email_normal(self):
        """Checking if user email is normalised"""
        email = "sanjana.maheshwari456@GMAIL.COM"
        user = get_user_model().objects(email,"test123")
        self.assertEqual(user.email,email.lower())
