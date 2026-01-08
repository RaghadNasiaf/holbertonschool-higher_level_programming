#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
Each element is rounded to two decimal places.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a divisor.

    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float).

    Returns:
        A new matrix containing the division results.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)

    for row in matrix:
        if not isinstance(row, list):
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

    # This handles float('inf') correctly as it will return 0.0
    return [[round(x / div, 2) for x in row] for row in matrix]
