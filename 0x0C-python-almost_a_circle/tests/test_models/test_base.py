#!/usr/bin/python3
"""
Module contains the TestBase Class
"""
import unittest
from models.base import Base
import json


class TestBase(unittest.TestCase):
    """
    contains unittests for the Base Class
    """
    def test_init(self):
        new = Base()
        self.assertEqual(new.id, 1)
        self.assertEqual(Base(7).id, 7)
        self.assertEqual(Base().id, 2)

    def test_to_json_string(self):
        list_dict = [{"hello": "yes"}, {"happy": "nope"}]
        self.assertEqual(
            Base.to_json_string(list_dict), json.dumps(list_dict))
        self.assertEqual(Base.to_json_string(None), "[]")
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_from_json_string(self):
        list_dict = [{"hello": "yes"}, {"happy": "nope"}]
        self.assertEqual(
            Base.from_json_string(json.dumps(list_dict)), list_dict)
        self.assertEqual(Base.from_json_string(None), [])
        self.assertEqual(Base.from_json_string(""), [])
