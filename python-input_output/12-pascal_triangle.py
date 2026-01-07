#!/usr/bin/python3
"""
Module for Task 12: Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal’s triangle of n.
    Returns an empty list if n <= 0.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Each row starts with 1
        current_row = [1]

        # Calculate middle elements based on the previous row
        for j in range(1, i):
            current_row.append(prev_row[j - 1] + prev_row[j])

        # Each row ends with 1
        current_row.append(1)
        triangle.append(current_row)

    return triangle
