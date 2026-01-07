#!/usr/bin/python3
"""
Module for Task 0: Function to read and print a text file.
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.
    Args:
        filename (str): The name of the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
