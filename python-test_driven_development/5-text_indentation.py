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
    # Skip initial spaces at the very beginning of the text
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n")
            i += 1
            # Skip all spaces following a punctuation mark
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
