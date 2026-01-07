#!/usr/bin/python3
"""
Module for Task 5: Saving an object to a file in JSON format.
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file using a JSON representation.
    Args:
        my_obj: The object to be serialized.
        filename (str): The name of the file to save to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
