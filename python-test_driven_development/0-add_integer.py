#!/usr/bin/python3
"""
This module provides a function for integer addition.
It includes validation for types and handles float to int casting.
"""


def add_integer(a, b=98):
    """
    Adds two integers. Floats are casted to integers before addition.

    Args:
        a: The first number (int or float).
        b: The second number (int or float, default is 98).

    Returns:
        The integer sum of a and b.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
