#!/usr/bin/python3

"""Module contains a class Square that defines a square"""


class Square:
    """class Square defines a square by:

        - Private instance attribute: size
        - Instantiation with optional size: def __init__(self, size=0):
            - size must be an integer, otherwise raise a TypeError exception
            with the message size must be an integer
            - if size is less than 0, raise a ValueError exception with the
            message size must be >= 0

    """
    def __init__(self, size=0):
        """Setter for the size private field"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
