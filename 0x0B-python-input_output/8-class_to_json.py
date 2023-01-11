#!/usr/bin/python3
"""
Module contains the class_to_json function
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure for JSON \
serialization of an object
    Prototype: def class_to_json(obj)
    """
    return dict(obj.__dict__)
