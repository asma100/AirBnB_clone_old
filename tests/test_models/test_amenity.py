#!/usr/bin/python3
"""test amenity class"""
import unittest
from models.amenity import Amenity
class TestAmenity(unittest.TestCase):
    """
    Test class for the Amenity class
    """
    def setUp(self):
        """Create a User instance before each test method."""
        self.amenity = Amenity()
    def test_init(self):
        """
        Test if the Amenity class is initialized properly
        """
        self.amenity = Amenity()
        self.assertEqual(self.amenity.name, "")
        