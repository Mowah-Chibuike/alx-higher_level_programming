#!/usr/bin/python3
"""
Module contains the write_file function
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file and returns the number of characters \
written
    Prototype: def write_file(file_name="", text="")
    write_file creates the file if it doesn't exist and overwrites the \
file if it does exist
    """
    with open(filename, 'w+', encoding="utf-8") as a_file:
        return a_file.write(text)
