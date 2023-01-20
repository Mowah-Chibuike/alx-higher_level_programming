#!/usr/bin/python3
"""
Module contains the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle is a subclass of the Base Class with the private instance \
attributes, each with their own setter and getter:
        - __width
        - __height
        - __x
        - __y
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
        getter for the width private instance attribute
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for the width private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 1:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """
        getter for the height private instance attribute
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for the height private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 1:
            raise ValueError('height must be > 0')
        self.__height = value

    @property
    def x(self):
        """
        getter for the x private instance attribute
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        setter for the x private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """
        getter for the y private instance attribute
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        setter for the width private instance attribute
        """
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """
        returns the area value of the Rectangle instance
        """
        return self.width * self.height

    def display(self):
        """
        prints to the stdout the Rectangle instance with the # character
        """
        for i in range(self.y):
            print()

        for i in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'.format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the Rectangle instance
        """
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    Base.__init__(self, value)
                elif i == 1:
                    self.width = value
                elif i == 2:
                    self.height = value
                elif i == 3:
                    self.x = value
                elif i == 4:
                    self.y = value
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
        Returns a dictionary representation of itself
        """
        attr_dict = {}
        attr_dict["id"] = self.id
        attr_dict["width"] = self.width
        attr_dict["height"] = self.height
        attr_dict["x"] = self.x
        attr_dict["y"] = self.y
        return attr_dict
