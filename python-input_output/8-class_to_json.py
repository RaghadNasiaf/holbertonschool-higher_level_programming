#!/usr/bin/python3
"""
Module for Task 8: Function that returns dictionary for JSON.
"""


def class_to_json(obj):
    """
    Returns the dictionary description with simple data structure
    for JSON serialization of an object.
    Args:
        obj: an instance of a Class.
    Returns:
        The dictionary representation of the object.
    """
    return obj.__dict__
