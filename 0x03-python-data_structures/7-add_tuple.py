#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        x = len(tuple_a) - 1
        for i in range(x, 3):
            tuple_a += (0,)
    if len(tuple_b) < 2:
        x = len(tuple_a) - 1
        for i in range(x, 3):
            tuple_b += (0,) 
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] +tuple_b[1]
    print("printer: {}".format(new_tuple))
    return new_tuple
