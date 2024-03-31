#!/usr/bin/python3
"""This module provides a class FileStorage that serializes instances to a JSON
and desirializes JSON file to instances"""
import json
import os


class FileStorage:
    """class FileStorage that serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = 'file.json'
    __objects: {}

    def all(self):
        """Returns a dictionary of models currently in storage"""
        return FileStorage.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileSTorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileSTorage.objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
                json.dump(temp, f)

    def reload(self):
       """Loads storage dictionary from file"""
       from models.base_model import BaseModel

       classes = {
               'BaseModel': BaseModel
               }

       try:
           temp = {}
           with open(FileStorage.__file_path, 'r') as f:
               temp = json.load(f)
               for key, val in temp.items():
                   self.all()[key] = classes[val['__class__']](**val)
       except FileNotFoundError:
           pass
