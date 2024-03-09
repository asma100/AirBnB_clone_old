#!/usr/bin/python3
"""test City class""""
import unittest
from models.city import City
class TestAmenity(unittest.TestCase):
    """
    Test class for the City class
    """
    def test_init(self):
        """
        Test if the City class is initialized properly

        """
        self.city = City()
        self.assertEqual(self.city.city_id, "")
        


