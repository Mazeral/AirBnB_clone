#!/usr/bin/env python3
import uuid
import datetime
from models import storage


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
    def __init__(self, *args, **kwargs):
        """Init function of the class"""
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key is not 'class':
                    setattr(self, key, value)
                    if key == 'created_at' or 'updated_at':
                        setattr(self, key, datetime.strptime
                                (datetime_str, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
        if self.created_at == self.updated_at:
            storage.new()

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
        print("[{}] [{}] {}".format("BaseClass", self.id, self.__dict__))

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
        self.updated_at = datetime.datetime.now()
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
        for key, item in self.__dict__:
            if isinstance(item, datetime):
                instance_dict[key] = item.isoformat()
            else:
                instance_dict[key] = item
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
