#!/usr/bin/python3
"""Unittest for the Amenity class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Set up the Amenity instance for each test case."""
        self.amenity = Amenity()

    def test_default_name(self):
        """Test if the default name of the Amenity instance is an empty
        string."""
        self.assertEqual(self.amenity.name, "")

    def test_set_name(self):
        """Test if the name of the Amenity instance can be set correctly."""
        self.amenity.name = "New Amenity"
        self.assertEqual(self.amenity.name, "New Amenity")
