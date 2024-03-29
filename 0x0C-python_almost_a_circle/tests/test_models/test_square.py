#!/usr/bin/python3
"""
Module contains the TestSquare class
"""
import unittest
from io import StringIO
from unittest.mock import patch
from models.square import Square


class TestSquare(unittest.TestCase):
    """
    contains tests for the square class
    """
    def setUp(self):
        self.square = Square(4, 1, 1, 89)

    def test_width_init(self):
        with self.assertRaises(TypeError, msg='width must be an integer'):
            Square('str')

        with self.assertRaises(TypeError, msg='width must be an integer'):
            Square(0.7)

        with self.assertRaises(ValueError, msg='width must be > 0'):
            Square(0)

        self.assertEqual(self.square.width, 4)

    def test_x_init(self):
        with self.assertRaises(TypeError, msg='x must be an integer'):
            Square(5, 'str')

        with self.assertRaises(TypeError, msg='x must be an integer'):
            Square(3, 0.5)

        with self.assertRaises(ValueError, msg='x must be >= 0'):
            Square(0, -1)

        self.assertEqual(self.square.x, 1)

    def test_y_init(self):
        with self.assertRaises(TypeError, msg='y must be an integer'):
            Square(3, 1, 'str')

        with self.assertRaises(TypeError, msg='y must be an integer'):
            Square(3, 5, 0.7)

        with self.assertRaises(ValueError, msg='y must be >= 0'):
            Square(3, 2, -1)

        self.assertEqual(self.square.y, 1)

    def test_area(self):
        self.assertEqual(self.square.area(), 16)
        self.assertEqual(Square(15).area(), 225)

    def test_display(self):
        expected = "\n ####\n ####\n ####\n ####\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            self.square.display()
            self.assertEqual(fake_out.getvalue(), expected)

    def test_str(self):
        expected = "[Square] (89) 1/1 - 4"
        self.assertEqual(str(self.square), expected)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            print(self.square, end="")
            self.assertEqual(fake_out.getvalue(), expected)

    def test_size(self):
        self.square.size = 9
        self.assertEqual(str(self.square), "[Square] (89) 1/1 - 9")
        with self.assertRaises(TypeError, msg='width must be an integer'):
            self.square.size = "9"

    def test_update_args(self):
        self.square.update(9)
        self.assertEqual(str(self.square), "[Square] (9) 1/1 - 4")
        self.square.update(9, 3)
        self.assertEqual(str(self.square), "[Square] (9) 1/1 - 3")
        self.square.update(9, 3, 5)
        self.assertEqual(str(self.square), "[Square] (9) 5/1 - 3")
        self.square.update(9, 3, 5, 0)
        self.assertEqual(str(self.square), "[Square] (9) 5/0 - 3")

    def test_update_args_errors(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            self.square.update(9, 0.7)

        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.square.update(9, 0)

        with self.assertRaises(TypeError, msg="x must be an integer"):
            self.square.update(9, 2, 3, 0.7)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            self.square.update(9, 2, 3, -1)

        with self.assertRaises(TypeError, msg="y must be an integer"):
            self.square.update(9, 2, 3, 'str')

        with self.assertRaises(ValueError, msg="y must be >= 0"):
            self.square.update(9, 2, 3, -1)

    def test_update_kwargs(self):
        self.square.update(id=9)
        self.assertEqual(str(self.square), "[Square] (9) 1/1 - 4")
        self.square.update(size=3)
        self.assertEqual(str(self.square), "[Square] (9) 1/1 - 3")
        self.square.update(x=0)
        self.assertEqual(str(self.square), "[Square] (9) 0/1 - 3")
        self.square.update(y=0)
        self.assertEqual(str(self.square), "[Square] (9) 0/0 - 3")
        self.square.update(4, id=10)
        self.assertEqual(str(self.square), "[Square] (4) 0/0 - 3")

    def test_update_kwargs_errors(self):
        with self.assertRaises(TypeError, msg="width must be an integer"):
            self.square.update(size=0.7)

        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.square.update(size=0)

        with self.assertRaises(TypeError, msg="x must be an integer"):
            self.square.update(x=0.7)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            self.square.update(x=-1)

        with self.assertRaises(TypeError, msg="y must be an integer"):
            self.square.update(y='str')

        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.square.update(y=-1)

    def test_dictionary(self):
        expected = {"id": 89, "size": 4, "x": 1, "y": 1}
        self.assertEqual(self.square.to_dictionary(), expected)
