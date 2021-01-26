#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import json
from models import base
Base = base.Base


class TestBase(unittest.TestCase):
    """check functionality of Base class"""
    def _too_many_args(self):
        """testing too many args to init"""
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def _no_id(self):
        """Testing id as None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def _id_set(self):
        """Testing id as not None"""
        b98 = Base(98)
        self.assertEqual(b98.id, 98)

    def _no_id_after_set(self):
        """Testing id as None after not None"""
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def _nb_private(self):
        """Testing nb_objects as a private instance attribute"""
        b = Base(3)
        with self.assertRaises(AttributeError):
            print(b.nb_objects)
        with self.assertRaises(AttributeError):
            print(b.__nb_objects)

    def _to_json_string(self):
        """Testing regular to json string"""
        Base._Base__nb_objects = 0
        d1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        d2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        json_s = Base.to_json_string([d1, d2])
        self.assertTrue(type(json_s) is str)
        d = json.loads(json_s)
        self.assertEqual(d, [d1, d2])

    def _empty_to_json_string(self):
        """Test for passing empty list"""
        json_s = Base.to_json_string([])
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def _None_to_json_String(self):
        """testting None to a json"""
        json_s = Base.to_json_string(None)
        self.assertTrue(type(json_s) is str)
        self.assertEqual(json_s, "[]")

    def _from_json_string(self):
        """Tests normal from_json_string"""
        json_str = '[{"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}, \
{"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}]'
        json_l = Base.from_json_string(json_str)
        self.assertTrue(type(json_l) is list)
        self.assertEqual(len(json_l), 2)
        self.assertTrue(type(json_l[0]) is dict)
        self.assertTrue(type(json_l[1]) is dict)
        self.assertEqual(json_l[0],
                         {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8})
        self.assertEqual(json_l[1],
                         {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0})

    def _frjs_empty(self):
        """Tests from_json_string  empty string"""
        self.assertEqual([], Base.from_json_string(""))

    def _frjs_None(self):
        """Testing from_json_string   none string"""
        self.assertEqual([], Base.from_json_string(None))
