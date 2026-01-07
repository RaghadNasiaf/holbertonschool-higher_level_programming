#!/usr/bin/python3
"""
Module for Task 2: Function that appends a string to a text file.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a UTF8 text file.
    Args:
        filename (str): The name of the file.
        text (str): The string to append.
    Returns:
        int: The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
