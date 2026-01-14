#!/usr/bin/python3
"""
This module provides a function for text indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    No space at the beginning or end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ".?:"
    skip_space = True

    for char in text:
        if skip_space and char == ' ':
            continue

        print(char, end="")
        skip_space = False

        if char in chars:
            print("\n")
            skip_space = True
