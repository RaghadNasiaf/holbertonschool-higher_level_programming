#!/usr/bin/python3
"""
Module for text indentation.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = (char + "\n\n").join([s.strip(" ") for s in text.split(char)])

    print("{}".format(text), end="")
