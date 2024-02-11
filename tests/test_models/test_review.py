"""Review unit tests"""
import unittest
from unittest import mock

from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test Review"""

    def setUp(self):
        """Set up for test"""
        self.review = Review()
        self.review.place_id = "place_1"
        self.review.user_id = "user_1"
        self.review.text = "Great place!"

    def test_inheritance(self):
        """test inheritance"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """test attributes"""
        self.assertTrue(hasattr(self.review, "place_id"))
        self.assertTrue(hasattr(self.review, "user_id"))
        self.assertTrue(hasattr(self.review, "text"))
        self.assertEqual(self.review.place_id, "place_1")
        self.assertEqual(self.review.user_id, "user_1")
        self.assertEqual(self.review.text, "Great place!")

    def test_to_dict(self):
        """test to_dict"""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(review_dict['place_id'], 'place_1')
        self.assertEqual(review_dict['user_id'], 'user_1')
        self.assertEqual(review_dict['text'], 'Great place!')

    @mock.patch('models.review.Review.save')
    def test_save(self, mock_save):
        """test save"""
        self.review.save()
        mock_save.assert_called_once()

    def test_str(self):
        """test str"""
        expected = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(expected, str(self.review))


if __name__ == "__main__":
    unittest.main()
