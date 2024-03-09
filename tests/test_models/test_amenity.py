#!/usr/bin/python3
"""test amenity class"""
import unittest
from models.amenity import Amenity
from datetime import datetime
class TestAmenity(unittest.TestCase):
    """
    Test class for the Amenity class
    """
    def setUp(self):
        """Create a Amenity instance before each test method."""
        self.amenity = Amenity()
    def test_name(self):
        """
        Test if the Amenity class is initialized properly
        """
        self.amenity.name = "name"
        self.assertEqual(self.amenity.name, "name")
    def test_name_at_start (self):
        self.assertEqual(self.amenity.name, "")
    def test_name_str(self):
        """
        Test if the Amenity class is stringified properly
        """
        self.assertEqual(str, type(self.amenity.name))
    def test_two_amenities_unique_ids(self):
        """
        Test if the two amenities have different ids
        """
        a1 = Amenity()
        a2 = Amenity()
        self.assertNotEqual(a1.id, a2.id)
    def test_create_time_type(self):
        """
        Test if the created_at attribute is a datetime object
        """
        self.assertIsInstance(self.amenity.created_at, datetime)
    def test_update_time_type(self):
        """
        Test if the updated_at attribute is a datetime object
        """
        self.assertIsInstance(self.amenity.updated_at, datetime)
        
