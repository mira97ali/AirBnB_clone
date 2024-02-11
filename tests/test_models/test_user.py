"""User unit tests"""
import unittest
from unittest import mock

from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """Test User"""
    def setUp(self):
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password"
        self.user.first_name = "First"
        self.user.last_name = "Last"

    def test_inheritance(self):
        """test inheritance"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """test attributes"""
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password")
        self.assertEqual(self.user.first_name, "First")
        self.assertEqual(self.user.last_name, "Last")

    def test_to_dict(self):
        """test to_dict"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(user_dict['email'], 'test@example.com')
        self.assertEqual(user_dict['password'], 'password')
        self.assertEqual(user_dict['first_name'], 'First')
        self.assertEqual(user_dict['last_name'], 'Last')

    @mock.patch('models.user.User.save')
    def test_save(self, mock_save):
        self.user.save()
        mock_save.assert_called_once()

    def test_str(self):
        expected = f"[User] ({self.user.id}) {self.user.__dict__}"
        self.assertEqual(expected, str(self.user))


if __name__ == "__main__":
    unittest.main()
