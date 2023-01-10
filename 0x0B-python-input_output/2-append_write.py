#!/usr/bin/python3
"""
Module contains the append_write function
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a file and returns the number of \
characters added.
    Prototype: def append_write(filename="", text="")
    append_write creates the file if it doesn't exist
    """
    with open(filename, 'a+', encoding='utf-8') as a_file:
        return a_file.write(text)
