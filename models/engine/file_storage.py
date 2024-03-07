#!/usr/bin/python3
"""Storage for AirBnb clone"""

import json


class FileStorage:
    """
    Class that serializes and deserializes a dictionary to a JSON file
    """
    __filePath = "file.json"
    __objects = {}
    def all(self):
        """Returns the dictionary of objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in objects the obj with key"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes objects to JSON file"""
        dictObj = {}
        for key, val in FileStorage.__objects.items():
            dictObj[key] = val.to_dict()
            with open(FileStorage.__filePath, "w", encoding="utf-8") as jsonF:
                json.dump(dictObj, jsonF)

    def reload(self):
        """Deserializes the JSON file to objects"""
        from models.base_model import BaseModel
        definedClasses = {'BaseModel': BaseModel}
        try:
            with open(FileStorage.__filePath, encoding="utf-8") as jsonStr:
                deserialized = json.load(jsonStr)
                for obj_values in deserialized.values():
                    clsName = obj_values["__class__"]
                    cls_obj = definedClasses[clsName]
                    self.new(cls_obj(**obj_values))
        except FileNotFoundError:
            pass
