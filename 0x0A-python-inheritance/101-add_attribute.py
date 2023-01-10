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
    if hasattr(obj, '__slots__'):
        raise TypeError("can't add new attribute")
    if type(obj) in [int, str, dict, set, list, type, object]:
        raise TypeError("can't add new attribute")

    setattr(obj, name, value)
