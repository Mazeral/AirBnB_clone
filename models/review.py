#!/usr/bin/env python3
from models.base_model import BaseModel


class Review(BaseModel):
    place_id: string = ""
    user_id: string = ""
    text: string = ""
