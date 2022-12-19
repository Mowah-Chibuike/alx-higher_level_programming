#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    n = 0
    #try:
    for i in range(x):
        if type(my_list[i]) is int:
            print(my_list[i], end="")
            n += 1
    print()
    #except IndexError:
       # raise IndexError("list index out of range")
    #finally:
    return n
