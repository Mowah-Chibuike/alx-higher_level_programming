#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print(f"{i:d}")
    else:
        print("{:0>2d}".format(i), end=", ")
