"""City unit tests"""
import unittest
from unittest import mock

from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """Test City"""

    def setUp(self):
        """Set up for test"""
        self.city = City()
        self.city.state_id = "state_1"
        self.city.name = "city_name"

    def test_inheritance(self):
        """test inheritance"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """test attributes"""
        self.assertTrue(hasattr(self.city, "state_id"))
        self.assertTrue(hasattr(self.city, "name"))
        self.assertEqual(self.city.state_id, "state_1")
        self.assertEqual(self.city.name, "city_name")

    def test_to_dict(self):
        """test to_dict"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(city_dict['state_id'], 'state_1')
        self.assertEqual(city_dict['name'], 'city_name')

    @mock.patch('models.city.City.save')
    def test_save(self, mock_save):
        """test save"""
        self.city.save()
        mock_save.assert_called_once()

    def test_str(self):
        """test str"""
        expected = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(expected, str(self.city))


if __name__ == "__main__":
    unittest.main()
