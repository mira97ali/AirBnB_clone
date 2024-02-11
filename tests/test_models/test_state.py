"""State unit tests"""
import unittest
from unittest import mock

from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """Test State"""

    def setUp(self):
        """Set up for test"""
        self.state = State()
        self.state.name = "state_name"

    def test_inheritance(self):
        """test inheritance"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """test attributes"""
        self.assertTrue(hasattr(self.state, "name"))
        self.assertEqual(self.state.name, "state_name")

    def test_to_dict(self):
        """test to_dict"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(state_dict['name'], 'state_name')

    @mock.patch('models.state.State.save')
    def test_save(self, mock_save):
        """test save"""
        self.state.save()
        mock_save.assert_called_once()

    def test_str(self):
        """test str"""
        expected = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(expected, str(self.state))


if __name__ == "__main__":
    unittest.main()
