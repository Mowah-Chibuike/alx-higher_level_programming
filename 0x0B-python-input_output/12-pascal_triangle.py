#!/usr/bin/python3
"""
Module contains the pascal_triangle function
"""


def pascal_triangle(n):
    """
    Prototype: def pascal_triangle(n)
    Returns a list of lists of integers representing the Pascal's triangle of\
 n
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1], [1, 1]]
    prev = pascal_triangle(n - 1)
    row = prev[n - 1]
    new_row = [1]
    for i in range(len(row) - 1):
        new_row.append(row[i] + row[i + 1])
    new_row.append(1)
    new = [[i for i in x] for x in prev]
    new.append(new_row)
    return new
