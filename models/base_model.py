#!/usr/bin/env python3
import uuid
import datetime
import models


class BaseClass:
    """The BaseClass for everyclass in this project
    
    Attributes:
        id: The id of the instance
        created_at: The creation date
        updated_at: The update date

    Methods:
        __str__: prints an string representation of the class
        save(self): update the instance attributes with current datetime
        to_dict(self): returns the dictionary values of instances obj

    """
    DATE_FORMAT = '%Y-%m-%dT%H:%M:%S.%f'
    def __init__(self, *args, **kwargs):
        """Init function of the class"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key in ("updated_at", "created_at"):
                    self.__dict__[key] = datetime.strptime(value, DATE_FORMAT)
                elif key[0] == "id":
                    self.__dict__[key] = str(value)
                else:
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        if self.created_at == self.updated_at:
            models.storage.new()

    def __str__(self):
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
        print("[{}] [{}] {}".format(self.__class__.name, self.id, self.__dict__))

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
        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):
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
        instance_dict = {}
        for key, item in self.__dict__.items():
            if key in ("created_at", "updated_at"):
                instance_dict[key] = item.isoformat()
            else:
                instance_dict[key] = item
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
