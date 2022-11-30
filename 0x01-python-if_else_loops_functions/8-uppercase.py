#!/usr/bin/python3

def uppercase(str):
    if str == "":
        print()
    for i in range(len(str)):
        if ord(str[i]) < ord('a') or ord(str[i]) > ord('z'):
            char = str[i]
        else:
            char = chr(ord(str[i]) - ord(' '))

        if i == len(str) - 1:
            char += "\n"
        print("{}".format(char), end="")
