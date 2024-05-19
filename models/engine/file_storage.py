#!/usr/bin/env python3
import json
import os
from models.user import User


class FileStorage:
    """A Class to Serialize and Deserialize classes"""
    __objects = {}
    __file_path = "file.json"

    def __init__(self):
        """The init function

        The init function of the class

        Args:
            self: The standard argument

        Returns:
            Nothing
        """
        self.classes = {"BaseModel": BaseModel, "User": User}

    def all(self):
        """Return all things in the file.json

        Goes to file.json and gives all the data
        Args:
            self: The standard parameter

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        return self.__objects

    def new(self, obj):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        with open(self.__file_path, 'w') as f:
            obj_dict = {key: obj.to_dict() for
                        key, obj in self.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """Summary line.

        Extended description of function.

        Args:
            param1 (int): Description of param1.
            param2 (str): Description of param2.

        Returns:
            bool: Description of return value.

        Raises:
            ValueError: Description of ValueError.

        """
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.loads(f.read())
                for value in obj_dict:
                    cls = value["__class__"]
                    self.new(eval(cls)(**value))
