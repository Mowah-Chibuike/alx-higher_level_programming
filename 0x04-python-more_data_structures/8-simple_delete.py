#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    if a_dictionary.get(key):
        a_dictionary.pop(key)
    return dict(a_dictionary.items())
