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
        """Test if the new method adds an object to the dictionary"""
        user = User()
        self.storage.new(user)
        key = "User." + str(user.id)
        self.assertEqual(self.storage.all(), {key: user})
    def test_save_reload(self):
        """Test if save and reload methods work correctly"""
        user = User()
        self.storage.new(user)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        key = "User." + str(user.id)
        self.assertEqual(new_storage.all(), {key: user})

    def test_reload_file_not_found(self):
        """Test if reload handles FileNotFoundError correctly"""
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_empty_file(self):
        """Test if reload handles an empty JSON file correctly"""
        with open(FileStorage._FileStorage__file_path, "w") as json_file:
            json_file.write("")
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})
    
      

if __name__ == '__main__':
    unittest.main()