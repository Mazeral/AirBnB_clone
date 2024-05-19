#!/usr/bin/env python3
import uuid
import datetime
from models import storage


class BaseClass:
    """The BaseClass for everyclass in this project"""
    def __init__(self, *args, **kwargs):
        """Init function of the class"""
        if len(kwargs) != 0:
            for key, value in kwargs:
                if key is not 'class':
                    setattr(self, key, value)
                    if key == 'created_at' or 'updated_at':
                        setattr(self, key, datetime.strptime
                                (datetime_str, '%Y-%m-%dT%H:%M:%S.%f'))
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        if self.created_at == self.updated_at:
            storage.new()

    def __str__(self):
        print("[{}] [{}] {}".format("BaseClass", self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        instance_dict = {}
        for key, item in self.__dict__:
            if isinstance(item, datetime):
                instance_dict[key] = item.isoformat()
            else:
                instance_dict[key] = item
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
