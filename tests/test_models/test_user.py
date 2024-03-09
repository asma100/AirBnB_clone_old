#!/usr/bin/python3
"""test user class"""  
import unittest
from models.user import User
class TestUser(unittest.TestCase):
    """
    Test class for the User class
    """
    

    
    def test_password(self):
        """
        Test if the User class is initialized properly
        """
        self.user = User()
        self.assertEqual(self.user.password, "")
    def test_email(self):  
        """
        Test if the User class is initialized properly
        """
        self.user = User()
        self.assertEqual(self.user.email, "")
    def test_first_name(self):
        """
        Test if the User class is initialized properly
        """
        self.user = User()
        self.assertEqual(self.user.first_name, "")
    def test_last_name(self):
        """
        Test if the User class is initialized properly
        """
        self.user = User()
        self.assertEqual(self.user.last_name, "")

    def test_two_amenities_unique_ids(self):
        a1 = User()
        a2 = User()
        self.assertNotEqual(a1.id, a2.id)
        