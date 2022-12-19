#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    n = 0
    try:
        for i in range(x):
            n += 1
            print(my_list[i], end="")
        print()
    except Exception:
        print()
    finally:
        return n
