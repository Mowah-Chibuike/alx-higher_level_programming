#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) < ord('a') or ord(str[i]) > ord('z'):
            char = str[i]
        else:
            char = chr(ord(str[i]) - ord(' '))

        if i == len(str) - 1:
            print("{}".format(char))
        else:
            print("{}".format(char), end="")
