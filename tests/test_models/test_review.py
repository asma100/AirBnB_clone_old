#!/usr/bin/python3
"""test review class"""  
import unittest
from models.review import Review
class TestReview(unittest.TestCase):
    """
    Test class for the Review class
    """
    def setUp(self):
      """Create a User instance before each test method."""
      self.review = Review()
    def test_place_id_test(self):
      """Test if the place_id attribute is set properly."""
      self.review.place_id = "place_id"
      self.assertEqual(self.review.place_id, "place_id")
    def test_place_id_str(self):
      """Test if the place_id attribute is stringified properly."""
      self.assertEqual(str, type(self.review.place_id))  
    def test_user_id_test(self):
      """Test if the user_id attribute is set properly."""
      self.review.user_id = "user_id"
      self.assertEqual(self.review.user_id, "user_id")
    def test_user_id_str(self):
      """Test if the user_id attribute is stringified properly."""
      self.assertEqual(str, type(self.review.user_id))
    def test_text_test(self):
      """Test if the text attribute is set properly."""
      self.review.text = "text"
      self.assertEqual(self.review.text, "text")
    def test_text_str(self):
      """Test if the text attribute is stringified properly."""
      self.assertEqual(str, type(self.review.text))
      