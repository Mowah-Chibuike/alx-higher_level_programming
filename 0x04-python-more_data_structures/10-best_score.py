#!/usr/bin/python3

def best_score(a_dictionary):
    res = max(list(new_dict.values()))
    return list(filter(lambda x: x[1] == res, list(new_dict.items())))[0][0]
