#!/usr/bin/python3
"""User module"""

from models import base_model


class User(base_model.BaseModel):
    """User Model"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
