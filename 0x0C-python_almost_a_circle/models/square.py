#!/usr/bin/python3
"""
Module contains the Square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square is a subclass of Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        Rectangle.__init__(self, size, size, x, y, id)

    def __str__(self):
        return '[Square] ({}) {}/{} - {}'.format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """
        getter for the size property
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        setter for the width and height of an instance
        """
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """
        updates the attributes of the Square instance
        """
        if args:
            for i, value in enumerate(args):
                if i == 0:
                    Rectangle.update(self, value)
                elif i == 1:
                    self.size = value
                elif i == 2:
                    self.x = value
                elif i == 3:
                    self.y = value
        else:
            attr_dict = {}
            for key, value in kwargs.items():
                if key == "size":
                    self.size = value
                else:
                    attr_dict[key] = value
            Rectangle.update(self, **attr_dict)

    def to_dictionary(self):
        """
        Returns dictionary representation of the instance
        """
        attr_dict = Rectangle.to_dictionary(self)
        for key in ["width", "height"]:
            attr_dict.pop(key)
        attr_dict["size"] = self.size
        return attr_dict
