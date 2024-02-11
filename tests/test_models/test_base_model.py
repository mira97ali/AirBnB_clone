#!/usr/bin/python3
"""testing the BaseModel"""
import unittest
from unittest import mock
import datetime

from models import base_model
from models.engine import file_storage


class TestBaseModel(unittest.TestCase):
    """unittests"""

    def setUp(self):
        """Actions before each test"""
        # Mock the whole class FileStorage
        self.mock_file_storage_instance = mock.MagicMock()
        self.mock_file_storage = mock.patch(
            "models.file_storage.FileStorage",
            self.mock_file_storage_instance,
        ).start()
        # Mock only __objects because it's acting weirdaaah
        self.mock_file_storage_objects = mock.patch.object(
            file_storage.FileStorage,
            "_FileStorage__objects",
            new_callable=lambda: {}
        )
        self.mock_file_storage_objects.start()

    def tearDown(self):
        """Actions after each test"""
        mock.patch.stopall()

    def test_uniq_id(self):
        """testing the uniqueness of IDs"""
        instance1 = base_model.BaseModel()
        instance2 = base_model.BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_create_update_date_equal(self):
        """testing if created_at and updated_at are equal"""
        instance = base_model.BaseModel()
        self.assertEqual(instance.created_at, instance.updated_at)

    def test_save_excution(self):
        """testing if the save method is excuted well"""
        instance0 = base_model.BaseModel()
        instance0.save()
        self.assertNotEqual(instance0.updated_at, instance0.created_at)

    def test_str_result(self):
        """testing the result of __str__"""
        instance3 = base_model.BaseModel()
        self.assertEqual(
            instance3.__str__(),
            f"[BaseModel] ({instance3.id}) {instance3.__dict__}"
        )

    def test_dicto(self):
        """testing the dicto method"""
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        instance = base_model.BaseModel()
        dicto = instance.to_dict()
        self.assertIn("__class__", dicto.keys())
        self.assertEqual(
            dicto["created_at"],
            instance.created_at.strftime(date_format)
        )
        self.assertEqual(
            dicto["updated_at"],
            instance.updated_at.strftime(date_format)
        )

    def test_kwargs_init(self):
        """testing if the kwargs work as expected"""
        kwargs_instance = base_model.BaseModel(
            id='56d43177-cc5f-4d6c-a0c1-e167f8c27337',
            created_at='2017-09-28T21:03:54.052298'
        )
        self.assertEqual(
            kwargs_instance.id,
            '56d43177-cc5f-4d6c-a0c1-e167f8c27337')
        self.assertIsInstance(kwargs_instance.created_at, datetime.datetime)
        testing_created_at = datetime.datetime.strptime(
            '2017-09-28T21:03:54.052298',
            '%Y-%m-%dT%H:%M:%S.%f'
        )
        self.assertEqual(kwargs_instance.created_at, testing_created_at)


if __name__ == "__main__":
    unittest.main()
