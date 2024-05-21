#!/usr/bin/python3
from models.base_model import BaseModel


class City(BaseModel):
    """Class City with some public attributes"""
    state_id: str = ""
    name: str = ""
