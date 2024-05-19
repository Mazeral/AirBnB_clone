#!/usr/bin/env python3
import json
import os
from models.user import User


class FileStorage:
    """A Class to Serialize and Deserialize classes"""
    __objects = {}
    __file_path = "file.json"

    def __init__(self):
        self.classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            obj_dict = {key: obj.to_dict() for
                        key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.loads(f.read())
                for value in obj_dict:
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
