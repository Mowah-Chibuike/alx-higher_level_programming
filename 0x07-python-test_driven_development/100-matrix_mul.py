#!/usr/bin/python3
"""
Module conatains a function matrix_mul and its helper functions
"""


def validate_matrix(matrix):
    """
    This function checks if its argument is a list of lists
    Prototype: def validate_matrix(matrix)
    It returns True if it's a lists of lists, otherwise False
    """
    for row in matrix:
        if type(row) is not list:
            return False
    return True


def check_if_empty(matrix):
    """
    Function checks if a matrix is empty i.e [] or [[]]
    Prototype: def check_if_empty(matrix)
    Returns True if empty and False otherwise
    """
    if matrix == [] or matrix == [[]]:
        return True
    return False


def check_row_type(matrix):
    """
    Function checks if a row of a matrix is a list of integers i.e int or \
floats
Prototype: def check_row_type(matrix)
Returns True if all rows are lists of integers, otherwise False
    """
    for row in matrix:
        if row == []:
            return False
        for i in row:
            if type(i) not in [int, float]:
                return False
    return True


def check_row_width(matrix):
    """
    Function checks if all rows of a matrix are of equal widths
    Prototype: def check_row_width(matrix)
    Returns True if all rows are of equal widths, otherwise False
    """
    for i in range(len(matrix) - 1):
        if len(matrix[i]) != len(matrix[i + 1]):
            return False
    return True


def get_column(matrix, index):
    """
    Function returns the column specified by the index argument
    Prototype: def get_column(matrix, index)
    Returns column specified by index which is a list of elments at the \
position specified by index in each of the rows
    """
    column = []
    for row in matrix:
        column.append(row[index])
    return column


def reduce_lists(list1, list2):
    """
    Function reduces two lists to an integer by summing the product of \
elments at every index of each lists
Prototype:  def reduce_lists(list1, list2)
    """
    res = 0
    for a, b in zip(list1, list2):
        res += a * b
    return res


def matrix_mul(m_a, m_b):
    """
    This function multiplies two matrices
    """
    if type(m_a) is not list:
        raise TypeError('m_a must be a list')
    elif type(m_b) is not list:
        raise TypeError('m_b must be a list')

    if not validate_matrix(m_a):
        raise TypeError('m_a must be a list of lists')
    elif not validate_matrix(m_b):
        raise TypeError('m_b must be a list of lists')

    if check_if_empty(m_a):
        raise ValueError("m_a can't be empty")
    elif check_if_empty(m_b):
        raise ValueError("m_b can't be empty")

    if not check_row_type(m_a):
        raise TypeError('m_a should contain only integers or floats')
    elif not check_row_type(m_b):
        raise TypeError('m_b should contain only integers or floats')

    if not check_row_width(m_a):
        raise TypeError('each row of m_a must be of the same size')
    elif not check_row_width(m_b):
        raise TypeError('each row of m_b must be of the same size')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    mult_matrix = []
    for row_a in m_a:
        new_row = []
        for i in range(len(m_b[0])):
            column = get_column(m_b, i)
            new_row.append(reduce_lists(row_a, column))
        mult_matrix.append(new_row)
    return mult_matrix
