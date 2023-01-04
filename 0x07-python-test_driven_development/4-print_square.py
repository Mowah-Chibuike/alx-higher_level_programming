#!/usr/bin/python3
"""
Module contains a function print_square that prints a square with the (#)
character
"""


def print_square(size):
    """
    Prints a square with the character #.

    Prototype: def print_square(size). Where size is the size length of the
    square. Size must be an integer, otherwise raises a TypeError exception
    with the message size must be an integer

    If size is less than 0, raises a ValueError exception with the message size
    must be >= 0. If size is a float and is less than 0, raises a TypeError
    exception with the message size must be an integer
    """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        print('#' * size)
