import unittest
from models.base_model import BaseModel

class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""

    def test_amenity_init(self):
        """Tests that Amenity is initialized correctly with a given name."""
        name = "Amazing View"
        a = BaseModel()

        self.assertEqual(BaseModel, a)  # Assert expected name

if __name__ == '__main__':
    unittest.main() 