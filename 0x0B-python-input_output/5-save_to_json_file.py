#!/usr/bin/python3
"""
Module contains the save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes an Object to a file, using a JSON representation.
    Prototype: def save_to_json_file(my_obj, filename)
    """
    with open(filename, "w+", encoding="utf-8") as json_file:
        json_file.write(json.dumps(my_obj))
