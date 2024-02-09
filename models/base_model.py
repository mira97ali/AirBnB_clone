#!/usr/bin/python3
"""BaseModel module"""
import uuid
import datetime
from models import storage


class BaseModel:
    """BaseModel"""
    DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"

    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs['id']
            self.created_at = datetime.datetime.strptime(
                kwargs['created_at'],
                self.DATE_FORMAT
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
        self.updated_at = datetime.datetime.utcnow()
        storage.save()

    def to_dict(self):
        dicto = self.__dict__.copy()
        dicto["__class__"] = self.__class__.__name__
        dicto["created_at"] = self.created_at.strftime(self.DATE_FORMAT)
        dicto["updated_at"] = self.updated_at.strftime(self.DATE_FORMAT)
        return dicto
