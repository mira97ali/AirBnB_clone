#!/usr/bin/python3
"""Store first object"""
import json


# List of allowed models
models = {
    "BaseModel": "base_model",
    "Amenity": "amenity",
    "City": "city",
    "Place": "place",
    "Review": "review",
    "State": "state",
    "User": "user",
}


class FileStorage:
    """ FileStorage that serializes instances to a JSON file
        and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        data = {
            key: value.to_dict()
            for key, value
            in FileStorage.__objects.items()
        }
        with open(FileStorage.__file_path, "w", encoding="utf-8") as db:
            json.dump(data, db, indent=4)

    def reload(self):
        try:
            with open(
                FileStorage.__file_path,
                "r",
                encoding="utf-8"
            ) as json_file:
                for obj_id, obj_dict in json.load(json_file).items():
                    class_name = obj_dict["__class__"]
                    module_path = f"models.{models[class_name]}"
                    module = __import__(module_path, fromlist=[class_name])
                    target_class = getattr(module, obj_dict["__class__"])
                    obj = target_class(**obj_dict)
                    FileStorage.__objects[obj_id] = obj
        except FileNotFoundError:
            pass
