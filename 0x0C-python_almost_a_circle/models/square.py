#!/usr/bin/python3
"""
Module contains the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square a subclass of the class Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        run when an instance is created
        """
        Rectangle.__init__(self, size, size, x, y, id)

    @property
    def size(self):
        """
        getter for the size property
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for the size property
        """
        if type(value) not in [int, float]:
            raise TypeError('width must be an integer')
        elif value < 1:
            raise ValueError('width must be > 0')
        self.width = self.height = value

    def __str__(self):
        """
        run when class is usedd with str function or printed with the print \
function
        """
        return "[Square] ({}) \
{}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        updates the attributes of the Square class
        """
        if len(args) > 0:
            Rectangle.update(
                self, args[0], args[1], args[1], args[2], args[3])
        else:
            new_dict = {}
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                else:
                    new_dict[key] = value
            Rectangle.update(self, **new_dict)

    def to_dictionary(self):
        rect = Rectangle.to_dictionary(self)
        for key in ["width", "height"]:
            rect.pop(key)
        rect["size"] = self.size
        return rect 
