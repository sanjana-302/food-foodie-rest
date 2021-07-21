from django.test import TestCase
from app.calc import add,subtract

class CalcTest(TestCase):
    # Sample Unit Test
    def test_add_numbers(self):
        """Test sum of two numbers"""
        self.assertEqual(add(4,3),7)
    def test_sub_numbers(self):
        """Test difference of two numbers"""
        self.assertEqual(subtract(4,3),1)