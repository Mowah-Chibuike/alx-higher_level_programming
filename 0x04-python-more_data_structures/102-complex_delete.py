#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    length = len(a_dictionary)
    while length > 0:
        for x, y in a_dictionary.items():
            if y == value:
                a_dictionary.pop(x)
                break
        length -= 1
    return dict(a_dictionary.items())
