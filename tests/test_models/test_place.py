#!/usr/bin/python3
"""Unit test for the Place class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def setUp(self):
        """Set up the test case by creating an instance of Place."""
        self.place = Place()

    def test_city_id(self):
        """Test that the initial value of city_id is an empty string."""
        self.assertEqual(self.place.city_id, "")

    def test_user_id(self):
        """Test that the initial value of user_id is an empty string."""
        self.assertEqual(self.place.user_id, "")

    def test_name(self):
        """Test that the initial value of name is an empty string."""
        self.assertEqual(self.place.name, "")

    def test_description(self):
        """Test that the initial value of description is an empty string."""
        self.assertEqual(self.place.description, "")

    def test_number_rooms(self):
        """Test that the initial value of number_rooms is 0."""
        self.assertEqual(self.place.number_rooms, 0)

    def test_number_bathrooms(self):
        """Test that the initial value of number_bathrooms is 0."""
        self.assertEqual(self.place.number_bathrooms, 0)

    def test_max_guest(self):
        """Test that the initial value of max_guest is 0."""
        self.assertEqual(self.place.max_guest, 0)

    def test_price_by_night(self):
        """Test that the initial value of price_by_night is 0."""
        self.assertEqual(self.place.price_by_night, 0)

    def test_latitude(self):
        """Test that the initial value of latitude is 0.0."""
        self.assertEqual(self.place.latitude, 0.0)

    def test_longitude(self):
        """Test that the initial value of longitude is 0.0."""
        self.assertEqual(self.place.longitude, 0.0)

    def test_amenity_ids(self):
        """Test that the initial value of amenity_ids is an empty list."""
        self.assertEqual(self.place.amenity_ids, [])
