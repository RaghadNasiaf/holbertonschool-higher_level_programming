#!/usr/bin/python3
"""
Module for Task 4: Function that returns an object represented by a JSON string.
"""
import json


def from_json_string(my_str):
    """
    Returns a Python data structure represented by a JSON string.
    Args:
        my_str (str): The JSON string to be deserialized.
    Returns:
        object: Python representation of the JSON string.
    """
    return json.loads(my_str)
