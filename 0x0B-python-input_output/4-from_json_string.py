#!/usr/bin/python3
"""
Module contains the from_json_string function
"""
import json


def from_json_string(my_str):
    """
    Returns an object(Python data structure) represented by a JSON string
    """
    return json.dumps(my_str)
