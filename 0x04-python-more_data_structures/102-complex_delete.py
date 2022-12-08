#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    for x, y in a_dictionary.items():
        if y == value:
            a_dictionary.pop(x)
    return dict(a_dictionary.items())
