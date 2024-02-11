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
            {"MockBaseModel.mock_id": mock_base_model}
        )

    def test_save_objects(self):
        """test the method save"""
        with mock.patch('builtins.open', mock.mock_open()) as mocked_file:
            instance = file_storage.FileStorage()
            instance.save()
            mocked_file.assert_called_once_with(
                "file.json",
                "w",
                encoding="utf-8")
            mocked_file().write.assert_called_once_with('{}')

    def test_reload_file_not_found(self):
        """test reload file not found"""
        instance = file_storage.FileStorage()
        with mock.patch('builtins.open', side_effect=FileNotFoundError):
            instance.reload()
            self.assertEqual(instance.all(), {})

    def test_reload_success(self):
        """test reload success"""
        tested_model = "BaseModel"
        mock_instance = {
            f"{tested_model}.e5442077-5777-4920-a253-ef15491f9f34": {
                "created_at": "2024-02-11T18:41:32.588120",
                "id": "e5442077-5777-4920-a253-ef15491f9f34",
                "updated_at": "2024-02-11T18:41:32.588377",
                "__class__": tested_model
            }
        }
        instance = file_storage.FileStorage()
        with mock.patch(
            'builtins.open',
            mock.mock_open(read_data=str(mock_instance))
        ) as mock_file:
            with mock.patch(
                'json.load',
                return_value=mock_instance
            ) as mock_json_load:
                file_storage.FileStorage.reload(self)
                mock_file.assert_called_once_with(
                    "file.json",
                    "r",
                    encoding="utf-8")
                self.assertEqual(len(instance.all()), 1)
                _instance = next(iter(instance.all()))
                self.assertEqual(
                    instance.all()[_instance].__class__.__name__,
                    tested_model
                )
                mock_json_load.assert_called_once()
