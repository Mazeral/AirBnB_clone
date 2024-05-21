#!/usr/bin/python3
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class with attributes"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
