"""Place unit tests"""
import unittest
from unittest import mock

from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """Test Place"""

    def setUp(self):
        """Set up for test"""
        self.place = Place()
        self.place.city_id = "city_1"
        self.place.user_id = "user_1"
        self.place.name = "place_name"
        self.place.description = "Description here"
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 4
        self.place.price_by_night = 100
        self.place.latitude = 10.0
        self.place.longitude = 20.0
        self.place.amenity_ids = ["Amenity_1", "Amenity_2"]

    def test_inheritance(self):
        """test inheritance"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """test attributes"""
        self.assertTrue(hasattr(self.place, "city_id"))
        self.assertTrue(hasattr(self.place, "user_id"))
        self.assertTrue(hasattr(self.place, "name"))
        self.assertTrue(hasattr(self.place, "description"))
        self.assertTrue(hasattr(self.place, "number_rooms"))
        self.assertTrue(hasattr(self.place, "number_bathrooms"))
        self.assertTrue(hasattr(self.place, "max_guest"))
        self.assertTrue(hasattr(self.place, "price_by_night"))
        self.assertTrue(hasattr(self.place, "latitude"))
        self.assertTrue(hasattr(self.place, "longitude"))
        self.assertTrue(hasattr(self.place, "amenity_ids"))
        self.assertEqual(self.place.city_id, "city_1")
        self.assertEqual(self.place.user_id, "user_1")
        self.assertEqual(self.place.name, "place_name")
        self.assertEqual(self.place.description, "Description here")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 4)
        self.assertEqual(self.place.price_by_night, 100)
        self.assertEqual(self.place.latitude, 10.0)
        self.assertEqual(self.place.longitude, 20.0)
        self.assertEqual(self.place.amenity_ids, ["Amenity_1", "Amenity_2"])

    def test_to_dict(self):
        """test to_dict"""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(place_dict['city_id'], 'city_1')
        self.assertEqual(place_dict['user_id'], 'user_1')
        self.assertEqual(place_dict['name'], 'place_name')
        self.assertEqual(place_dict['description'], 'Description here')
        self.assertEqual(place_dict['number_rooms'], 3)
        self.assertEqual(place_dict['number_bathrooms'], 2)
        self.assertEqual(place_dict['max_guest'], 4)
        self.assertEqual(place_dict['price_by_night'], 100)
        self.assertEqual(place_dict['latitude'], 10.0)
        self.assertEqual(place_dict['longitude'], 20.0)
        self.assertEqual(place_dict['amenity_ids'], ["Amenity_1", "Amenity_2"])

    @mock.patch('models.place.Place.save')
    def test_save(self, mock_save):
        """test save"""
        self.place.save()
        mock_save.assert_called_once()

    def test_str(self):
        """test str"""
        expected = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(expected, str(self.place))


if __name__ == "__main__":
    unittest.main()
