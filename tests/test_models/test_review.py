#!/usr/bin/python3
"""Unit test for the Review class"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test the Review class"""

    def setUp(self):
        """Set up the test case by initializing a Review instance."""
        self.review = Review()

    def test_place_id(self):
        """Test the place_id attribute of the Review class."""
        self.assertEqual(self.review.place_id, "")

    def test_user_id(self):
        """Test the user_id attribute of the Review class."""
        self.assertEqual(self.review.user_id, "")

    def test_text(self):
        """Test the text attribute of the Review class."""
        self.assertEqual(self.review.text, "")
