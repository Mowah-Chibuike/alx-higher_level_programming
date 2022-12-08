#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for x, y in dict(sorted(list(a_dictionary.items()))).items():
        print("{}: {}".format(x, y))
