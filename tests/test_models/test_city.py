#!/usr/bin/python3
"""Unittest for the City class"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test case for the City class."""

    def test_city_state_id(self):
        """Test the state_id property of the City class."""
        city = City()
        city.state_id = ["CA", None]
        self.assertEqual(city.state_id[0], "CA")
        self.assertIsNone(city.state_id[1])

    def test_city_name(self):
        """Test the name property of the City class."""
        city = City()
        city.name = ["San Francisco", None]
        self.assertEqual(city.name[0], "San Francisco")
        self.assertIsNone(city.name[1])
