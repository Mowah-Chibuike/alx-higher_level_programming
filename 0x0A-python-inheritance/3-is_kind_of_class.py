#!/usr/bin/python3
"""
Module contains the function called is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Prototype: def is_kind_of_class(obj, a_class)
    Returns True if obj is an instance of, or if obj is an instance of a \
class that inherited from, the a_class ; otherwise False.
    """
    return issubclass(obj, a_class)
