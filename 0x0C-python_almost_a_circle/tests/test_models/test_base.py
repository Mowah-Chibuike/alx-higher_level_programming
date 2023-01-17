#!/usr/bin/python3
"""
Module contains tests for the Base class
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    contains tests for the Base Class
    """
    def test_1(self):
        self.assertEqual(Base().id, 1)
        self.assertEqual(Base(7).id, 7)
        self.assertEqual(Base().id, 2)
