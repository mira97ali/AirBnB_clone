#!/usr/bin/python3
"""BaseModel module"""
import uuid
import datetime


class BaseModel:
    """BaseModel"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.utcnow()
        self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.datetime.utcnow()

    def to_dict(self):
        dicto = self.__dict__
        dicto["__class__"] = self.__class__.__name__
        dicto["created_at"] = self.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        dicto["updated_at"] = self.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
        return dicto
