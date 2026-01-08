#!/usr/bin/python3
"""
This module provides a function that divides all elements of a matrix.
It handles validation for matrix structure, element types, and divisor.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given divisor.
    All elements are rounded to 2 decimal places.
    
    Args:
        matrix: A list of lists of integers or floats.
        div: A number (integer or float) to divide by.
        
    Returns:
        A new matrix containing the divided elements.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    
    if not isinstance(matrix, list) or not matrix or not matrix[0]:
        raise TypeError(msg)

    row_size = len(matrix[0])
    
    for row in matrix:
        if not isinstance(row, list) or not row:
            raise TypeError(msg)
        if len(row) != row_size:
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, (int, float)):
                raise TypeError(msg)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(x / div, 2) for x in row] for row in matrix]
