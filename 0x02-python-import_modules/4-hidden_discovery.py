#!/usr/bin/python3

import hidden_4


def print_names():
    names = dir(hidden_4)
    for i in names:
        if i[:2] != "__":
            print("{}".format(i))


if __name__ == "__main__":
    print_names()
