#!/usr/bin/python3
"""
Unittest for base_model
"""

import unittest
import models
from models.base_model import BaseModel
from datetime import datetime
class TestBaseModel(unittest.TestCase):
    """
    Test class for the BaseModel class
    """
    def setUp(self):
        """
        Set up method that runs before each test
        """
        self.base_model = BaseModel()
    
    def test_two_amenities_unique_ids(self):
        """
        Test if the two amenities have different ids
        """
        a1 = BaseModel()
        a2 = BaseModel()
        self.assertNotEqual(a1.id, a2.id)
    def test_create_time_type(self):
        """
        Test if the created_at attribute is a datetime object
        """
        self.assertIsInstance(self.base_model.created_at, datetime)
    def test_update_time_type(self):
        """
        Test if the updated_at attribute is a datetime object
        """
        self.assertIsInstance(self.base_model.updated_at, datetime)
    def test_str_method(self):
        """Tests method is printing """
        b1 = BaseModel()
        b1printed = b1.__str__()
        self.assertEqual(b1printed,
                         "[BaseModel] ({}) {}".format(b1.id, b1.__dict__))
    def test_attribute(self):
        """Tests if the instance of BaseModel have been correctly made"""
        self.assertTrue(hasattr(self.base_model, "__init__"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))
        self.assertTrue(hasattr(self.base_model, "id"))
