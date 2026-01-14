#!/usr/bin/python3
"""
This module provides a function for text indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    There should be no space at the beginning or at the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Character-by-character processing to manage whitespaces
    res = ""
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue

        res += char
        skip_space = False

        if char in ".?:":
            res += "\n\n"
            skip_space = True

    # Print the result while ensuring no extra spaces at start/end of lines
    print("\n".join([line.strip() for line in res.split("\n")]), end="")
