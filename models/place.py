#!/usr/bin/env python3
from models.base_model import BaseModel


class Place(BaseModel):
    """Place Class with attributes"""
    city_id: string = ""
    user_id: string = ""
    name: string = ""
    description: string = ""
    number_rooms: integer = 0
    number_bathrooms: integer = 0
    max_guest: integer = 0
    price_by_night: integer = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids = []
