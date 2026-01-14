#!/usr/bin/python3
"""
This module provides a function to check if an object is an instance of,
or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an
    instance of a class that inherited from, the specified class;
    otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to match against.

    Returns:
        bool: True if obj is an instance or inherited instance, else False.
    """
    return isinstance(obj, a_class)
