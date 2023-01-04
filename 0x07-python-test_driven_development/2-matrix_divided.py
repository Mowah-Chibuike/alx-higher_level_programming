#!/usr/bin/python3
"""
Module contains function matrix_divided that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
        Prototype: def matrix_divided(matrix, div)
        - matrix_divided divides all elements of a matrix.

        - matrix must be a list of lists of integers or floats, otherwise
        raises a TypeError exception with the message matrix must be a matrix
        (list of lists) of integers/floats

        - Each row of the matrix must be of the same size, otherwise raises a
        TypeError exception with the message Each row of the matrix must have
        the same size

        - div must be a number (integer or float), otherwise raises a
        TypeError exception with the message div must be a number

        - All elements of the matrix should be divided by div, rounded to 2
        decimal places

        - Returns a new matrix
    """
    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of integers/floats')
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                    'matrix must be a matrix (list of lists) of integers/' +
                    'floats')
        for column in row:
            if type(column) not in [int, float]:
                raise TypeError(
                        'matrix must be a matrix (list of lists) of integers' +
                        '/floats')
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            raise TypeError('Each row of the matrix must have the same size')
    if type(div) not in [int, float]:
        raise TypeError('div must be a number')
    elif div == 0:
        raise ZeroDivisionError('division by zero')
    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            result = i / div
            new_row.append(result.__round__(2))
        new_matrix.append(new_row)
    return new_matrix
