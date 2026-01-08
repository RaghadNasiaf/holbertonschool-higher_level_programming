#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
Each result is rounded to two decimal places.
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

    # 1. Check if matrix is a list of lists
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(msg)
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(msg)

    # 2. Check if all rows have the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # 3. Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # 4. Check if div is zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # 5. Validate matrix elements are numbers and perform division
    new_matrix = []
    for row in matrix:
        new_row = []
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)
            # Handle float('inf') correctly: result rounded to 2 places
            new_row.append(round(x / div, 2))
        new_matrix.append(new_row)

    return new_matrix
