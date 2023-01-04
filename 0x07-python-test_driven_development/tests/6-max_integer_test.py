#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(max_integer(), None)
        self.assertEqual(max_integer([]), None)

    def test_one_max(self):
        self.assertEqual(max_integer([1, 4, 3, 2]), 4)
        self.assertEqual(max_integer([10, 45, 57, 2]), 57)

    def test_two_max(self):
        self.assertEqual(max_integer([1, 55, 55, 2]), 55)
        self.assertEqual(max_integer([23, 45, 67, 67]), 67)

    def test_only_floats(self):
        self.assertEqual(max_integer([0.1, 0.2, 0.3, 0.4]), 0.4)
        self.assertEqual(max_integer([11.5, 55.6, 33.9, 100.0]), 100.0)

    def test_negative_int(self):
        self.assertEqual(max_integer([-1, -15, -45, -23]), -1)
        self.assertEqual(max_integer([-0.3, -0.9, -0.5, -0.1]), -0.1)

    def test_both_int_float(self):
        self.assertEqual(max_integer([1, 0.9, 7, 8.9]), 8.9)

    def test_both_positive_negative(self):
        self.assertEqual(max_integer([-1, 5, 9, -2]), 9)
