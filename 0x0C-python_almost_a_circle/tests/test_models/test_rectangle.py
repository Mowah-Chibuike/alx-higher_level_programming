#!/usr/bin/python3
"""
Module contains the TestRectangle class
"""
import json
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """
    contains tests for the Rectangle class
    """
    def setUp(self):
        self.rect = Rectangle(2, 3, 1, 1, 89)

    def test_width_init(self):
        with self.assertRaises(TypeError, msg='width must be an integer'):
            Rectangle('str', 1)

        with self.assertRaises(TypeError, msg='width must be an integer'):
            Rectangle(0.7, 5)

        with self.assertRaises(ValueError, msg='width must be > 0'):
            Rectangle(0, 2)

        self.assertEqual(self.rect.width, 2)

    def test_height_init(self):
        with self.assertRaises(TypeError, msg='height must be an integer'):
            Rectangle(1, 'str')

        with self.assertRaises(TypeError, msg='height must be an integer'):
            Rectangle(1, 0.2)

        with self.assertRaises(ValueError, msg='height must be > 0'):
            Rectangle(2, 0)

        self.assertEqual(self.rect.height, 3)

    def test_x_init(self):
        with self.assertRaises(TypeError, msg='x must be an integer'):
            Rectangle(5, 4, 'str')

        with self.assertRaises(TypeError, msg='x must be an integer'):
            Rectangle(3, 5, 0.5)

        with self.assertRaises(ValueError, msg='x must be >= 0'):
            Rectangle(0, 2, -1)

        self.assertEqual(self.rect.x, 1)

    def test_y_init(self):
        with self.assertRaises(TypeError, msg='y must be an integer'):
            Rectangle(3, 1, 1, 'str')

        with self.assertRaises(TypeError, msg='y must be an integer'):
            Rectangle(3, 5, 1, 0.7)

        with self.assertRaises(ValueError, msg='y must be >= 0'):
            Rectangle(3, 2, 2, -1)

        self.assertEqual(self.rect.y, 1)

    def test_area(self):
        self.assertEqual(self.rect.area(), 6)
        self.assertEqual(Rectangle(15, 5).area(), 75)

    def test_display(self):
        expected = "\n ##\n ##\n ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.rect.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_str(self):
        expected = "[Rectangle] (89) 1/1 - 2/3"
        self.assertEqual(str(self.rect), expected)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(self.rect, end="")
            self.assertEqual(fake_out.getvalue(), expected)

    def test_update_args(self):
        self.rect.update(9)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 1/1 - 2/3")
        self.rect.update(9, 3)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 1/1 - 3/3")
        self.rect.update(9, 3, 5)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 1/1 - 3/5")
        self.rect.update(9, 3, 5, 0)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 0/1 - 3/5")
        self.rect.update(9, 3, 5, 0, 0)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 0/0 - 3/5")

    def test_update_args_errors(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            self.rect.update(9, 0.7)

        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.rect.update(9, 0)

        with self.assertRaises(TypeError, msg="height must be an integer"):
            self.rect.update(9, 5, 0.7)

        with self.assertRaises(ValueError, msg="height must be > 0"):
            self.rect.update(9, 2, 0)

        with self.assertRaises(TypeError, msg="x must be an integer"):
            self.rect.update(9, 2, 3, 0.7)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            self.rect.update(9, 2, 3, -1)

        with self.assertRaises(TypeError, msg="y must be an integer"):
            self.rect.update(9, 2, 3, 0, 'str')

        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.rect.update(9, 2, 3, 0, -1)

    def test_update_kwargs(self):
        self.rect.update(id=9)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 1/1 - 2/3")
        self.rect.update(width=3)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 1/1 - 3/3")
        self.rect.update(height=5)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 1/1 - 3/5")
        self.rect.update(x=0)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 0/1 - 3/5")
        self.rect.update(y=0)
        self.assertEqual(str(self.rect), "[Rectangle] (9) 0/0 - 3/5")
        self.rect.update(4, id=10)
        self.assertEqual(str(self.rect), "[Rectangle] (4) 0/0 - 3/5")

    def test_update_kwargs_errors(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            self.rect.update(width=0.7)

        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.rect.update(width=0)

        with self.assertRaises(TypeError, msg="height must be an integer"):
            self.rect.update(height=0.7)

        with self.assertRaises(ValueError, msg="height must be > 0"):
            self.rect.update(height=0)

        with self.assertRaises(TypeError, msg="x must be an integer"):
            self.rect.update(x=0.7)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            self.rect.update(x=-1)

        with self.assertRaises(TypeError, msg="y must be an integer"):
            self.rect.update(y='str')

        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.rect.update(y=-1)

    def test_dictionary(self):
        expected = {"id": 89, "width": 2, "height": 3, "x": 1, "y": 1}
        self.assertEqual(self.rect.to_dictionary(), expected)

    def test_save_to_file(self):
        expected = Rectangle.to_json_string([
            {"y": 8, "x": 2, "id": 89, "width": 10, "height": 7},
            {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}])
        r1 = Rectangle(10, 7, 2, 8, 89)
        r2 = Rectangle(2, 4, 0, 0, 2)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r", encoding='utf-8') as a_file:
            self.assertEqual(json.loads(a_file.read()), json.loads(expected))

    def test_load_from_file(self):
        expected = [
                {"y": 8, "x": 2, "id": 89, "width": 10, "height": 7},
                {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
        from_file = Rectangle.load_from_file()
        list_obj = [item.to_dictionary() for item in from_file]
        self.assertEqual(list_obj, expected)
        with open("Rectangle.json", "w+", encoding='utf-8') as a_file:
            pass
        self.assertEqual(Rectangle.load_from_file(), [])
