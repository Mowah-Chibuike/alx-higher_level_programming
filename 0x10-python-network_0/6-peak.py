#!/usr/bin/python3
"""
Contains find_peak function definition
"""


def find_peak(integers):
    """
    returns one of the peaks of a  list of unsorted integers
    """
    length = len(integers)
    if integers is None or length == 0:
        return None

    low = 0
    high = length - 1
    while low < high:
        mid = (high + low) // 2
        if integers[mid + 1] < integers[mid]:
            high = mid
        else:
            low = mid + 1
    return integers[low]
