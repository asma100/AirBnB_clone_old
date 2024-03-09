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
    __file_path = "file.json"
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
        return FileStorage.__objects

    def new(self, obj):
        """Sets in objects the obj with key"""
        if obj:
            key = obj.__class__.__name__ + "." + str(obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON file"""
        dictObj = {}
        for key, val in FileStorage.__objects.items():
            dictObj[key] = val.to_dict()
            with open(FileStorage.__file_path, "w", encoding="utf-8") as jsonF:
                json.dump(dictObj, jsonF)

    def reload(self):
        """Deserializes the JSON file to objects"""
        try:
            with open(self.__file_path, encoding="utf-8") as fi:
                objdict = json.loads(fi.read())
            for value in objdict.values():
                clsName = value["__class__"]
                self.new(eval(clsName)(**value))
        except FileNotFoundError:
            pass
