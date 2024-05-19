#!/usr/bin/env python3
from models import BaseModel


class User(BaseModel):
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
