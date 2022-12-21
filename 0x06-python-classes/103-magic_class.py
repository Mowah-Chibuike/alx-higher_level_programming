#!/usr/bin/python3
"""Module holds a class named MagicClass"""
import math


class MagicClass:
    """Initializes class MagicClass by:

        - Public instance method: def area(self): that returns the circle area
        - Public instance method: def circumference(self): that returns the
        circle perimeter
    """
    def __init__(self, radius=0):
        if type(radius) is not float and type(radius) is not int:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        return (2 * math.pi * self.__radius)
