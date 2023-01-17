#!/usr/bin/python3
"""
Module contains the Rectangle Class
"""
from models.base import Base


class Rectangle(Base):
    """
    Class Rectangle inherits from the Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        runs whenever a new instance is created
        """
        Base.__init__(self, id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        getter for the width private instance variable
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the width private instance variable
        """
        if type(value) not in [int, float]:
            raise TypeError('width must be an integer')
        elif value < 1:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        getter for the height private instance variable
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the height private instance variable
        """
        if type(value) not in [int, float]:
            raise TypeError('height must be an integer')
        elif value < 1:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        getter for the x private instance variable
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for the x private instance variable
        """
        if type(value) not in [int, float]:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        getter for the y private instance variable
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for the y private instance variable
        """
        if type(value) not in [int, float]:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        for i in range(self.y):
            print()

        for i in range(self.height):
            print(" " * self.x, '#' * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} \
- {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates the instance of the Rectangle class
        """
        if len(args) > 0:
            Base.__init__(self, args[0])
            self.width = args[1]
            self.height = args[2]
            self.x = args[3]
            self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    Base.__init__(self, value)
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """
        returns a dictionary representation of a Rectangle instance with the \
following keys
            - id
            - width
            - height
            - x
            - y
        """
        dict_repr = {}
        dict_repr["id"] = self.id
        dict_repr["width"] = self.width
        dict_repr["height"] = self.height
        dict_repr["x"] = self.x
        dict_repr["y"] = self.y
        return dict_repr
