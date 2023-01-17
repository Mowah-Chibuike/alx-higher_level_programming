#!/usr/bin/python3
"""
Module contains tests for the Rectangle Class
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    creates tests for the Rectangle Class
    """
    def test_init(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            Rectangle('str', 2)

        with self.assertRaises(TypeError, msg="height must be an integer"):
            Rectangle(2, 'str')

        rect = Rectangle(1, 2)
        self.assertEqual(rect.width, 1)
        self.assertEqual(rect.x, 0)
        rect = Rectangle(3, 4)
        with self.assertRaises(ValueError, msg="width must be > 0"):
            Rectangle(0, 2)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            Rectangle(2, 3, -1)

        rect = Rectangle(8, 9, 0, 0, 3)
        self.assertEqual(rect.id, 3)

    def test_area(self):
        self.assertEqual(Rectangle(2, 3).area(), 6)
        self.assertEqual(Rectangle(5, 15).area(), 75)

    def test_str_(self):
        self.assertEqual(
            Rectangle(2, 3, 0, 0, 5).__str__(), "[Rectangle] (5) 0/0 - 2/3")
