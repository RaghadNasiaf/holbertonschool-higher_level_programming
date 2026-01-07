#!/usr/bin/python3
"""
Module for Task 3: Function that returns the JSON representation of an object.
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    Args:
        my_obj: The object to be serialized.
    Returns:
        str: JSON string representation of my_obj.
    """
    return json.dumps(my_obj)
