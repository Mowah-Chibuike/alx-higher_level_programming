#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    booleans = [True, False]
    return [booleans[x % 2] for x in my_list]
