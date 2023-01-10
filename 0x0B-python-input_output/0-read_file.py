#!/usr/bin/python3
"""
Module contains the read_file function
"""


def read_file(filename=""):
    """
    Reads a text file(UTF8) and prints it to the stdout
    Prototype: def read_file(filename="")
    """
    with open(filename, encoding="utf-8") as a_file:
        for line in a_file:
            print(line, end="")
