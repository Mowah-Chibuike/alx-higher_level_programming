#!/usr/bin/python3
"""
Module contains a BaseGeometry class
"""


class BaseGeometry(object):
    """
    BaseGeometry class
    Public instance method: def area(self): that raises an exception with the\
 message area() is not implemented
    Public instance method: def integer_validator(self, name, value): that \
validates value:
        - if value is not an integer: raises a TypeError exception, with the \
message <name> must be an integer
        - if value is less or equal to 0: raise a ValueError exception with \
the message <name> must be greater than 0
    """
    def area(self):
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        Validates the value argument
        """
        if type(value) not in [int]:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be greater than 0'.format(name))
