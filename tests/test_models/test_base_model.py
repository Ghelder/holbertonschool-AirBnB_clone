"""Module for testing the BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel class"""

    def testOfClass(self):
        """Test for the __init__ method"""
        b1 = BaseModel()
        b1.name = "My First Model"
        self.assertEqual(b1.name, b1.name)
