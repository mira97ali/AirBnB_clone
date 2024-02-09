#!/usr/bin/python3
"""testing the FileStorage"""
import unittest
from unittest import mock

from models.engine import file_storage


class MockBaseModel(mock.Mock):
    """Mock Base Model"""
    id = "mock_id"

    def to_dict(self):
        return {"id": self.id}


class TestFileStorage(unittest.TestCase):
    """unittests"""

    def setUp(self):
        """Actions to do after test finished"""
        self.mock_file_storage_objects = mock.patch.object(
            file_storage.FileStorage,
            "_FileStorage__objects",
            new_callable=lambda: {}
        )
        self.mock_file_storage_objects.start()

    def tearDown(self):
        """Actions after each test"""
        mock.patch.stopall()

    def test_file_storage_all_objects(self):
        """test if the method all returns all objects"""
        instance = file_storage.FileStorage()
        self.assertEqual(instance.all(), {})

    def test_add_to_objects(self):
        """test if the element is added to __objects"""
        instance = file_storage.FileStorage()
        mock_base_model = MockBaseModel()
        instance.new(mock_base_model)
        self.assertNotEqual(instance.all(), {})
        self.assertEqual(
            instance.all(),
            {"mock_id": {"id": "mock_id"}}
        )

    def test_save_objects(self):
        """test the method save"""
        with mock.patch('builtins.open', mock.mock_open()) as mocked_file:
            instance = file_storage.FileStorage()
            instance.save()
            mocked_file.assert_called_once_with("file.json", 'w', encoding="utf-8")
            mocked_file().write.assert_called_once_with('{}')

    def test_reload_file_not_found(self):
        instance = file_storage.FileStorage()
        with mock.patch('builtins.open', side_effect=FileNotFoundError):
            instance.reload()
            self.assertEqual(instance.all(), {})

    def test_reload_success(self):
        instance = file_storage.FileStorage()
        with mock.patch('builtins.open', mock.mock_open(read_data='{"key": "value"}')) as mock_file:
            with mock.patch('json.load', return_value={"key": "value"}) as mock_json_load:
                file_storage.FileStorage.reload(self)
                mock_file.assert_called_once_with("file.json", "r", encoding="utf-8")
                self.assertDictEqual(instance.all(), {"key": "value"})
                mock_json_load.assert_called_once()
