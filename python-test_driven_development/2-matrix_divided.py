#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor (div).
    Args:
        matrix (list): List of lists of integers or floats.
        div (int/float): The number to divide by.
    Returns:
        A new matrix with results rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(msg)
        if not all(isinstance(val, (int, float)) for val in row):
            raise TypeError(msg)

    row_len = len(matrix[0])
    if not all(len(row) == row_len for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(val / div, 2) for val in row] for row in matrix]

