#!/usr/bin/python3

def best_score(a_dictionary):
    if isinstance(a_dictionary, dict) and len(a_dictionary):
        res = max(list(a_dictionary.values()))
        for x, y in a_dictionary.items():
            if y == res:
                return x
