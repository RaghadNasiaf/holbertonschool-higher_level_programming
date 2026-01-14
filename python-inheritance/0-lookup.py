#!/usr/bin/python3
"""
This module provides a function to lookup object attributes and methods.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing attributes and methods.
    """
    return dir(obj)
