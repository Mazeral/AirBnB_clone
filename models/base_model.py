import uuid
import datetime


class BaseClass:
    """The BaseClass for everyclass in this project"""
    def __init__(self, arg):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        print("[{}] [{}] {}".format("BaseClass", self.id, self.__dict__))

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        instance_dict = {}
        for key, item in self.__dict__:
            if isinstance(item, datetime):
                instance_dict[key] = item.isoformat()
            else:
                instance_dict[key] = item
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
