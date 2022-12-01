#!/usr/bin/python3

import sys


def print_args():
    """print_args function: Prints arguments of the program"""
    argv = sys.argv
    length = len(argv)
    if length > 2:
        print("{:d} arguments:".format(length - 1))
    elif length == 2:
        print("{:d} argument:".format(length - 1))
    else:
        print("{:d} arguments.".format(length - 1))

    for i in range(1, length):
        print("{:d} : {}".format(i, argv[i]))


if __name__ == "__main__":
    print_args()
