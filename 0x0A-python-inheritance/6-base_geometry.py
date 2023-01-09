#!/usr/bin/python3
"""
Module contains a BaseGeometry class
"""


class BaseGeometry(object):
    """
    BaseGeometry class
    Public instance method: def area(self): that raises an exception with the\
 message area() is not implemented
    """
    def area(self):
        raise Exception('area() is not implemented')
