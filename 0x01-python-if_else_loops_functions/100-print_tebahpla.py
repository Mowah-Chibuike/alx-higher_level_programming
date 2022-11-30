#!/usr/bin/python3

start = ord("z")
for i in range(26):
    alphabet = start - i
    if i % 2 == 1:
        alphabet -= ord(' ')

    print("{}".format(chr(alphabet)), end="")
