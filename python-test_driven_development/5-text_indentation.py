#!/usr/bin/python3
"""
This module provides a function for text indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    There should be no space at the beginning or end of each line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)

    # Skip leading spaces
    while i < length and text[i] == ' ':
        i += 1

    while i < length:
        print(text[i], end="")

        if text[i] in ".?:":
            # Skip spaces after punctuation
            i += 1
            while i < length and text[i] == ' ':
                i += 1

            # Print new lines ONLY if there is more text to print
            if i < length:
                print("\n")
            continue

        i += 1
