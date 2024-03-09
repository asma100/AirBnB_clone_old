import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models.place import Place  

class TestFileStorage(unittest.TestCase):
    """
    Test class for the FileStorage class
    """  
    def setUp(self):
        """
        Set up method that runs before each test
        """
        self.storage = FileStorage()  
    def test_all(self):
        """
        Test if the FileStorage class is initialized properly
        """
        self.assertEqual(self.storage.all(), {})
    def test_new(self):
        """
        Test if the FileStorage class is initialized properly
        """
        user = User(**{"email": "tugrp@example.com"})
        self.storage.new(user)
        self.assertEqual(self.storage.all(), {"User.1": user})
    def test_save(self):
        """
        Test if the FileStorage class is initialized properly
        """
        self.storage.new(User, "user_id", {"email": "tugrp@example.com"})
        self.storage.save()
        self.assertEqual(self.storage.all(), {"user_id": {"email": "tugrp@example.com"}})
    def test_reload(self):
        """
        Test if the FileStorage class is initialized properly
        """
        self.storage.new(User, "user_id", {"email": "tugrp@example.com"})
        self.storage.save()
        self.storage.reload()
        self.assertEqual(self.storage.all(), {"user_id": {"email": "tugrp@example.com"}})
    def test_delete(self):
        """
        Test if the FileStorage class is initialized properly
        """
        self.storage.new(User, "user_id", {"email": "tugrp@example.com"})
        self.storage.save()
        self.storage.delete("user_id")
        self.assertEqual(self.storage.all(), {})
    
      

if __name__ == '__main__':
    unittest.main()