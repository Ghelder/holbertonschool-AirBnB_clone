#!/usr/bin/python3
"""Loads and reloads the file storage."""

import json


class FileStorage:
    """serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_objects = {}
        for key, value in self.__objects.items():
            json_objects[key] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(json_objects, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        from models.base_model import BaseModel
        from models.user import User
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.state import State

        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                file_load = json.load(f)
            for key, value in file_load.items():
                self.__objects[key] = eval(value["__class__"])(**value)
        except FileNotFoundError:
            pass
