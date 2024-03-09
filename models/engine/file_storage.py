#!/usr/bin/python3
"""Storage for AirBnb clone"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    Class that serializes and deserializes a dictionary to a JSON file
    """
    __filePath = "file.json"
    __objects = {}
    definedClasses = {'BaseModel': BaseModel,
                      'User': User,
                      'State': State,
                      'City': City,
                      'Amenity': Amenity,
                      'Place': Place,
                      'Review': Review}

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Sets in objects the obj with key"""
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON file"""
        dictObj = {}
        for key, val in self.__objects.items():
            dictObj[key] = val.to_dict()
            with open(self.__filePath, "w", encoding="utf-8") as jsonF:
                json.dump(dictObj, jsonF)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                new_obj_dict = json.load(f)
            for key, value in new_obj_dict.items():
                obj = self.class_dict[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
