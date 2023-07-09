"""Module for testing the BaseModel class"""

import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test for the BaseModel class"""

    def test_init(self):
        """Test the initialization of the BaseModel"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        """Test the string representation of the BaseModel"""
        model = BaseModel()
        expected_output = (
            f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        )
        actual_output = str(model)
        self.assertEqual(actual_output, expected_output)

    def test_save(self):
        """Test the save method of the BaseModel"""
        model = BaseModel()
        old_created_at = model.created_at
        old_updated_at = model.updated_at
        model.save()
        new_created_at = model.created_at
        new_updated_at = model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(old_created_at, new_created_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel"""
        model = BaseModel()
        obj_dict = model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], model.updated_at.isoformat())
