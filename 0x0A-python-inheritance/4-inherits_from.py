#!/usr/bin/python3
"""
Module contains the function called inherits_from
"""


def inherits_from(obj, a_class):
    """
    Prototype: def inherits_from(obj, a_class)
    Returns True if obj is an instance of a class that inherited(directly or \
indirectly) from a_class; otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
