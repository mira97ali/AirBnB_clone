#!/usr/bin/python3
"""Review module"""

from models import base_model


class Review(base_model.BaseModel):
    """Review Model"""
    place_id = ""
    user_id = ""
    text = ""
