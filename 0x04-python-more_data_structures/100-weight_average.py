#!/usr/bin/python3

def weight_average(my_list=[]):
    total = n = 0
    for x, y in my_list:
        total += x * y
        n += y
    return total / n
