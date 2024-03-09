#!/usr/bin/python3
"""Base Model for AirBnb clone"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel():
    """Represnts the base model"""
    def __init__(self, *args, **kwargs):
        """Initializes a new model
        Args:
            id: id of the model.
            created_at: date of creation.
            updated_at: date of updates.
        """
        if kwargs:
            del kwargs['__class__']
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Returns the dictionary"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates the updated_at instance and saves it"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        map_objects = {}
        for key, value in self.__dict__.items():
            if key == "created_at" or key == "updated_at":
                map_objects[key] = value.isoformat()
            else:
                map_objects[key] = value
        map_objects["__class__"] = self.__class__.__name__
        return map_objects
