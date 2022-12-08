#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total = n = 0
    for x, y in my_list:
        total += x * y
        n += y
    return total / n
