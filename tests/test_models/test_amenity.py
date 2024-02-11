"""Amenity unit tests"""
import unittest
from unittest import mock

from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """Test Amenity"""
    def setUp(self):
        self.amenity = Amenity()
        self.amenity.name = "Pool"

    def test_inheritance(self):
        """test inheritance"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """test attributes"""
        self.assertTrue(hasattr(self.amenity, "name"))
        self.assertEqual(self.amenity.name, "Pool")

    def test_to_dict(self):
        """test to_dict"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(amenity_dict['name'], 'Pool')

    @mock.patch('models.amenity.Amenity.save')
    def test_save(self, mock_save):
        """test save"""
        self.amenity.save()
        mock_save.assert_called_once()

    def test_str(self):
        """test str"""
        expected = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(expected, str(self.amenity))


if __name__ == "__main__":
    unittest.main()
