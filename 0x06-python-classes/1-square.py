#!/usr/bin/python3

"""Module creates a class named Square"""


class Square:
    """Class Square defines a square by:
        - Private instance attribute: size
        - Instantiation with size (no type/value verification)

    """
    def __init__(self, size):
        self.__size = size
