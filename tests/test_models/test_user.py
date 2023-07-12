#!/usr/bin/python3
"""Test class User"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test the User class"""

    def test_default_values(self):
        """Test the default values of the User class"""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_set_values(self):
        """Test the set values of the User class"""
        user = User()
        user.email = "test@example.com"
        user.password = "password123"
        user.first_name = "John"
        user.last_name = "Doe"

        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "password123")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
