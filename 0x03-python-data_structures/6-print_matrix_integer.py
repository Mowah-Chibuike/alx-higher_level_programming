#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        delim = ""
        for i in row:
            print("{}{:d}".format(delim, i), end="")
            delim = " "
        print()
