#!/usr/bin/python3
"""Store first object"""
import json


class FileStorage:
    """ FileStorage that serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        FileStorage.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj.to_dict()

    def save(self):
        with open(FileStorage.__file_path, "w", encoding="utf-8") as db:
            json.dump(FileStorage.__objects, db, indent=4)

    def reload(self):
        try:
            with open(
                FileStorage.__file_path,
                "r",
                encoding="utf-8"
            ) as json_file:
                FileStorage.__objects = json.load(json_file)
        except FileNotFoundError:
            pass
