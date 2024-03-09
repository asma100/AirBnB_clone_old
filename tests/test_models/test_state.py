#!/usr/bin/python3
"""test City class"""
import unittest
from models.city import City
from datetime import datetime
class TestAmenity(unittest.TestCase):
    """
    Test class for the City class
    """
    def setUp(self):
        """Create a City instance before each test method."""
        self.city = City()
    def test_city_id(self):
        """
        Test if the City class is initialized properly
        """
        self.city.state_id = "state_id"
        self.assertEqual(self.city.state_id, "state_id")
    def test_city_id_str(self):
        """
        Test if the City class is stringified properly
        """
        self.assertEqual(str, type(self.city.state_id))
    def test_two_cities_unique_ids(self):
        """
        Test if the two cities have different ids
        """
        a1 = City()  
        a2 = City()
        self.assertNotEqual(a1.id, a2.id)
    def test_create_time_type(self):
        """
        Test if the created_at attribute is a datetime object
        """
        self.assertIsInstance(self.city.created_at, datetime)
    def test_update_time_type(self):
        """
        Test if the updated_at attribute is a datetime object 
        """
        self.assertIsInstance(self.city.updated_at, datetime)
        