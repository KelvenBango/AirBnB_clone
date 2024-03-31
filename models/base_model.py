#!/usr/bin/python3
"""Defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime

class BaseModel:
    """Base class for all hbnb models"""
    def __init__(self, *args, **kwargs):
        """initializes instance attributes"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
            
            self.__dict__.update(kwargs)


    def __str__(self):
        """Returns a tring representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return f'[{cls}] ({self.id}) {self.__dict__}'

    def save(self):
        """updates the attribute updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update(
                {'__class__':
                (str(type(self)).split('.')[-1]).split('\'')[0]
                })
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        return dictionary

