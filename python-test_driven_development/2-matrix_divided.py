#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It ensures that the input is a valid matrix of numbers and a valid divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).

    Returns:
        A new matrix containing the division results rounded to 2 decimal places.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(msg)

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
