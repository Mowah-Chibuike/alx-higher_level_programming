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
        - Private instance attribute: position:
            - property def position(self): to retrieve it
            - property setter def position(self, value): to set it:
                position must be a tuple of 2 positive integers, otherwise
                raise a TypeError exception with the message position must be
                a tuple of 2 positive integers
        - Instantiation with size and optional position:
        def __init__(self, size=0, position=(0, 0))
        - Public instance method: def area(self): that returns the current
        square area
        - Public instance method: def my_print(self): that prints in stdout
        the square with the character #:
            - if size is equal to 0, prints an empty line

    """
    def __init__(self, size=0, position=(0,0)):
        """Initializer of every instance of the class Square"""
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Returns the position private field of instance"""
        return self.__position

    @position.setter
    def position(self, position):
        """Setter for the position private field"""
        for i in position:
            if isinstance(i, int) is False:
                raise TypeError('position must be a tuple of 2 positive' + 
                'integers')
        self.__position = position

    def area(self):
        """Returns the area of the square"""
        return(self.__size ** 2)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
            return

        for i in range(self.__position[1]):
            print()

        for i in range(self.__size):
            for i in range(self.__position[0]):
                print(' ', end='')
            print('#' * self.__size)
