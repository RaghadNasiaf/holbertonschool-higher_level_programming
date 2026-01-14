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

    # Clean the string from start/end spaces
    text = text.strip()
    
    # Flags to manage spaces and punctuation
    skip_space = False
    
    for i in range(len(text)):
        if skip_space and text[i] == ' ':
            continue
        
        print(text[i], end="")
        skip_space = False
        
        if text[i] in ".?:":
            print("\n")
            skip_space = True
