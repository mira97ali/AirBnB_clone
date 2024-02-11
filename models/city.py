#!/usr/bin/python3
"""City module"""

from models import base_model


class City(base_model.BaseModel):
    """City Model"""
    state_id = ""
    name = ""
