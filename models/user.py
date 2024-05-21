#!/usr/bin/python3
from models.base_model import BaseModel


class User(BaseModel):
    """User Class which inherites from BaseModel"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
