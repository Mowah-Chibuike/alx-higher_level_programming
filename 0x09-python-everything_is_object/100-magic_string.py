#!/usr/bin/python3
def func():
    count = globals()['i'] if globals().get('i') else 0
    return ("BestSchool, " * count) + "BestSchool"
