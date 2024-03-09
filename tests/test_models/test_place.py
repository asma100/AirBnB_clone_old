#!/usr/bin/python3
"""test place class"""

import unittest
from models.place import Place
class TestPlace(unittest.TestCase):  
    """
    Test class for the Place class
    """
    def setUp(self):
        """Create a Place instance before each test method."""  
        self.place = Place()  
    def test_c_id(self):  
        """Test if the place_id attribute is set properly."""  
        self.place.city_id = "city_id"  
        self.assertEqual(self.place.city_id, "city_id")
    def test_c_id_str(self):  
        """Test if the place_id attribute is stringified properly."""  
        self.assertEqual(str, type(self.place.city_id))
    def test_u_id(self):  
        """Test if the user_id attribute is set properly."""  
        self.place.user_id = "user_id"  
        self.assertEqual(self.place.user_id, "user_id")
    def test_u_id_str(self):
        """Test if the user_id attribute is stringified properly."""  
        self.assertEqual(str, type(self.place.user_id))
    def test_name(self):
        """Test if the name attribute is set properly."""  
        self.place.name = "name"  
        self.assertEqual(self.place.name, "name")
    def test_name_str(self):
        """Test if the name attribute is stringified properly."""  
        self.assertEqual(str, type(self.place.name))
    def test_description(self):
        """Test if the description attribute is set properly."""  
        self.place.description = "description"  
        self.assertEqual(self.place.description, "description")
    def test_description_str(self):
        """Test if the description attribute is stringified properly."""  
        self.assertEqual(str, type(self.place.description))
    def test_number_rooms(self):
        """Test if the number_rooms attribute is set properly."""  
        self.place.number_rooms = 0
        self.assertEqual(self.place.number_rooms, 0) 
    def test_number_rooms_int(self):
        """Test if the number_rooms attribute is stringified properly."""  
        self.assertEqual(int, type(self.place.number_rooms))
    def test_number_bathrooms(self):
        """Test if the number_bathrooms attribute is set properly."""  
        self.place.number_bathrooms = 0
        self.assertEqual(self.place.number_bathrooms, 0)
    def test_number_bathrooms_int(self):
        """Test if the number_bathrooms attribute is stringified properly."""  
        self.assertEqual(int, type(self.place.number_bathrooms))
    def test_max_guest(self):
        """Test if the max_guest attribute is set properly."""  
        self.place.max_guest = 0
        self.assertEqual(self.place.max_guest, 0)
    def test_max_guest_int(self):
        """Test if the max_guest attribute is stringified properly."""  
        self.assertEqual(int, type(self.place.max_guest))
    def test_price_by_night(self):
        """Test if the price_by_night attribute is set properly."""  
        self.place.price_by_night = 0
        self.assertEqual(self.place.price_by_night, 0)
    def test_price_by_night_int(self):
        """Test if the price_by_night attribute is stringified properly."""  
        self.assertEqual(int, type(self.place.price_by_night))
    def test_latitude(self):
        """Test if the latitude attribute is set properly."""  
        self.place.latitude = 0.0
        self.assertEqual(self.place.latitude, 0.0)
    def test_latitude_float(self):
        """Test if the latitude attribute is stringified properly."""  
        self.assertEqual(float, type(self.place.latitude))
    def test_longitude(self):
        """Test if the longitude attribute is set properly."""  
        self.place.longitude = 0.0
        self.assertEqual(self.place.longitude, 0.0)
    def test_longitude_float(self):
        """Test if the longitude attribute is stringified properly."""  
        self.assertEqual(float, type(self.place.longitude))
    def test_amenity_ids(self):
        """Test if the amenity_ids attribute is set properly."""  
        self.place.amenity_ids = []
        self.assertEqual(self.place.amenity_ids, [])
    def test_amenity_ids_list(self):
        """Test if the amenity_ids attribute is stringified properly."""  
        self.assertEqual(list, type(self.place.amenity_ids))
        