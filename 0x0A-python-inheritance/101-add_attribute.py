#!/usr/bin/python3
"""
Module contains a function called add_attribute
"""


def add_attribute(obj, name, value):
    """
    Function adds a new attribute to a function if possible
    Prototype: def add_attribute(obj, name, value)
    Raises a TypeError exception if the object can't have the new attribute
    """
    if not hasattr(obj, '__setattr__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, name):
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
