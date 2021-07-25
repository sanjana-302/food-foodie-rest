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
        user = get_user_model().objects.create_user(email,"test123")
        self.assertEqual(user.email,email.lower())

    def test_new_user_invalid_email(self):
        """Checking if user has a valid email address"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,"test123")
    
    def test_create_new_super_user(self):
        """Checks for new super user created"""
        user = get_user_model().objects.create_user(
            "test@gmail.com",
            "test123"
        )
        user.is_superuser = True
        user.is_staff = True

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)