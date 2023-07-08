#!/usr/bin/python3
"""Defines the BaseModel class"""
import uuid
from datetime import datetime


class BaseModel:
    """Base class for all AirBnB models"""

    def __init__(self, **kwargs):
        """Initializes a BaseModel instance.

        Args:
            kwargs (dict): Optional keyword arguments to set instance
            attributes.
        """
        if kwargs:
            self.set_attributes_from_kwargs(kwargs)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def set_attributes_from_kwargs(self, kwargs):
        """Sets instance attributes from a dictionary.

        Args:
            kwargs (dict): Dictionary containing attribute-value pairs.
        """
        for key, value in kwargs.items():
            # if key == "created_at" or key == "updated_at":
            if key in ("created_at", "updated_at"):
                setattr(self, key, self.parse_datetime(value))
            elif key != "__class__":
                setattr(self, key, value)

    def parse_datetime(self, value):
        """Sets instance attributes from a dictionary.

        Args:
            kwargs (dict): Dictionary containing attribute-value pairs.
        """
        return datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")

    def __str__(self):
        """Returns a string representation of the BaseModel object."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates the `updated_at` attribute with the current datetime."""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Converts the BaseModel object to a dictionary representation."""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
