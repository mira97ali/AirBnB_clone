#!/usr/bin/python3
"""BaseModel module"""
import uuid
import datetime
from models import storage


DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """BaseModel"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.datetime.strptime(
                kwargs['created_at'],
                DATE_FORMAT
            )
            self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.utcnow()
            self.updated_at = self.created_at
            storage.new(self)

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update and Save"""
        storage.save()

    def to_dict(self):
        """To Dictionary"""
        dicto = {}
        for key in dir(self):
            if key.startswith("_"):
                continue
            value = getattr(self, key)
            if not callable(value):
                dicto[key] = value
        dicto["__class__"] = self.__class__.__name__
        dicto["created_at"] = self.created_at.strftime(DATE_FORMAT)
        dicto["updated_at"] = self.updated_at.strftime(DATE_FORMAT)
        return dicto
