#!/usr/bin/python3
"""
Module contains function say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Function that prints My name is <first name> <last name>
    - Prototype: def say_my_name(first_name, last_name="")
    - first_name and last_name must be strings otherwise, raises a TypeError
    exception with the message first_name must be a string or last_name must
    be a string
    """
    if isinstance(first_name, str) is False:
        raise TypeError('first_name must be a string')
    elif isinstance(last_name, str) is False:
        raise TypeError('last_name must be a string')
    print('My name is {} {}'.format(first_name, last_name))
