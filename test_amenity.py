import unittest
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    """Unit tests for the Amenity class."""

    def test_amenity_init(self):
        """Tests that Amenity is initialized correctly with a given name."""
        name = "Amazing View"
        amenity = Amenity(name)

        self.assertEqual(amenity.name, name)  # Assert expected name

if __name__ == '__main__':
    unittest.main()      
        