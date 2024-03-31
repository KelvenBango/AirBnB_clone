#!/usr/bin/python3
"""This module defines a test class for base model"""
from models.base_model import BaseModel
from datetime import datetime
import unittest
import os

class test_basemodel(unittest.TestCase):
    """Defines a class for testcases"""
    def setUp(self):
        """Setup the basemodel class"""
        self.model = BaseModel()

    def tearDown(self):
        """"""
        pass

    def test_id(self):
        """Test that id is initialized properly"""
        self.assertIsNotNone(self.model.id)
    
    def test_created_at(self):
        """Test created_at attributte is initialized properly"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attributte is initialized properly"""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """Test that verify that the string representation is formatted correctly"""
        expected_output = f'[{BaseModel.__name__}] ({self.model.id}) {self.model.__dict__}'
        self.assertEqual(str(self.model), expected_output)

    def test_save_method(self):
        """Test that updated changes after calling the save method"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Ensure that the dictionary returned contains all attribures
        and their values
        """
        object_dictionary = self.model.to_dict()
        self.assertIn('__class__', object_dictionary)
        self.assertEqual(object_dictionary['__class__'], 'BaseModel')
        self.assertIn('created_at', object_dictionary)
        self.assertIn('updated_at', object_dictionary)
        self.assertEqual(
                object_dictionary['created_at'],
                self.model.created_at.isoformat()
                )
        self.assertEqual(object_dictionary['updated_at'],
                self.model.updated_at.isoformat()
                )

    def test_init_with_kwargs(self):
        """Test initialization with keyword arguments"""
        args = {
            'id': 'test_id',
            'created_at': '2024-03-31T12:00:00.000000',
            'updated_at': '2024-03-31T12:00:00.000000'
        }
        model = BaseModel(**args)
        self.assertEqual(model.id, 'test_id')
        self.assertEqual(model.created_at, datetime(2024, 3, 31, 12, 0))
        self.assertEqual(model.updated_at, datetime(2024, 3, 31, 12, 0))

if __name__ == "__main__":
    unittest.main()
