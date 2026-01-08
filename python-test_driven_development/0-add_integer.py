#!/usr/bin/python3
"""
This module provides a function that adds two integers.
The integers can be positive, negative, or floats.
"""


def add_integer(a, b=98):
    """
    Adds two integers.
    Args:
        a: The first number.
        b: The second number, defaults to 98.
    Returns:
        The sum of a and b as an integer.
    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
