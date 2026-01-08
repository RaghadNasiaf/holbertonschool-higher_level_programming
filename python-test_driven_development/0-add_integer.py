#!/usr/bin/python3
"""
This module provides a simple function to add two numbers.
The function ensures that inputs are integers or floats,
and casts them to integers before performing the addition.
It is designed to demonstrate test-driven development practices.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting them to integers.

    Args:
        a: The first number, must be an int or float.
        b: The second number, must be an int or float. Defaults to 98.

    Returns:
        The integer result of adding a and b.

    Raises:
        TypeError: If either a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
