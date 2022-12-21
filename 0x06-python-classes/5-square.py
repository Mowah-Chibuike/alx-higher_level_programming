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
        - Public instance method: def my_print(self): that prints in stdout
        the square with the character #:
            - if size is equal to 0, prints an empty line

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

    def area(self):
        """Returns the area of the square"""
        return(self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print('#' * self.__size)
