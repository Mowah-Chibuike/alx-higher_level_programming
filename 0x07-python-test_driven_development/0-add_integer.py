#!/usr/bin/python3
"""
Module contains function: add_integer that adds two integers
"""


def add_integer(a, b=98):
    """
    Function adds two integers.
    a and b must be integers or floats
    Returns an integer: addition of a and b
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return int(a) + int(b)
