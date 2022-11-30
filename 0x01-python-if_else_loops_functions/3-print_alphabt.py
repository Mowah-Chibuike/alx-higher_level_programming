#!/usr/bin/python3

alphabet = ord("a")
for i in range(26):
    if (alphabet != ord("q") and alphabet != ord("e")):
        print("{}".format(chr(alphabet)), end="")
    alphabet += 1
