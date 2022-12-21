#!/usr/bin/python3

"""Module contains a class Square"""


class Square:
    """class Square defines a square by:

        - Private instance attribute: size:
            - property def size(self): to retrieve it
            - property setter def size(self, value): to set it:
                - size must be an integer, otherwise raises a TypeError
                exception with the message 'size must be an integer'
                - if size is less than 0, raises a ValueError exception with
                the message 'size must be >= 0'
        - Instantiation with size: def __init__(self, size=0)
        - Public instance method: def area(self): that returns the current
        square area

    """
    def __init__(self, size=0):
        """Initializer of every instance of the class Square"""
        self.size = size

    @property
    def size(self):
        """Returns the size private field of instance"""
        return self.__size

    @size.setter
    def size(self, size):
        """Setter for the size private field"""
        if isinstance(size, int) is False:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size

    def __new__(self, value):
        return value ** 2

    def area(self):
        """Returns the area of the square"""
        return (self.__size ** 2)
