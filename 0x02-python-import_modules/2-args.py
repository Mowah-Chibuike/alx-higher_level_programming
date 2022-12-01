#!/usr/bin/python3

import sys


argv = sys.argv
length = len(argv)
if length > 2:
    print("{:d} arguments:".format(length - 1))
else:
    print("{:d} argument.".format(length - 1))

for i in range(1, length):
    print("{:d} : {}".format(i, argv[i]))
