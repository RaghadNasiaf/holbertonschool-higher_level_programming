#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Args:
        matrix: list of lists of integers/floats.
        div: number (int/float) to divide by.
    Returns:
        A new matrix with values rounded to 2 decimal places.
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if matrix is None or not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(error_msg)

    for row in matrix:
        if not isinstance(row, list) or len(row) == 0:
            raise TypeError(error_msg)
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(error_msg)
if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if div == float('inf') or div == float('-inf'):
        return [[0.0 for _ in row] for row in matrix]

    return [[round(val / div, 2) for val in row] for row in matrix]

