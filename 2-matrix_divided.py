#!/usr/bin/python3
"""Module for matrix division"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a divisor"""
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    row_len = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)
    return [[round(x / div, 2) for x in row] for row in matrix]
