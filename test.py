#!/usr/bin/python3
"""test state class"""  
import unittest  
from models.state import State
from datetime import datetime
class TestState(unittest.TestCase):
    """
    Test class for the State class
    """
    def setUp(self):
      """Create a State instance before each test method."""  
      self.state = State()  
    def test_name (self):
        """
        Test if the State class is initialized properly
        """
        self.state.name = "name"
        self.assertEqual(self.state.name, "name")
    def test_name_str(self):
        """
        Test if the State class is stringified properly  
        """
        self.assertEqual(str, type(self.state.name))
    def test_two_state_unique_ids(self):
        a1 = State()
        a2 = State()
        self.assertNotEqual(a1.id, a2.id)
    def test_create_time_type(self):
        """
        Test if the created_at attribute is a datetime object
        """
        self.assertIsInstance(self.state.created_at, datetime)
    def test_update_time_type(self):
        """
        Test if the updated_at attribute is a datetime object 
        """
        self.assertIsInstance(self.state.updated_at, datetime)



if __name__ == '__main__':
    unittest.main()