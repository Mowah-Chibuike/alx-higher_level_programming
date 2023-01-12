#!/usr/bin/python3
"""
Module contains the append_after function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line containing specific \
string
    """
    with open(filename, 'r', encoding='utf-8') as f:
        f.seek(0, 0)
        data = f.readlines()

    i = 0
    while i < len(data):
        line = data[i]
        if search_string in line:
            data[i] += new_string
        i += 1

    with open(filename, 'w', encoding='utf-8') as f:
        for line in data:
            f.write(line)
