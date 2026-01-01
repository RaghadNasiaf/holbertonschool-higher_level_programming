#!/usr/bin/python3
"""
This module provides a specialized class for handling list operations.
The primary objective is to demonstrate how to create a subclass that
extends the features of the standard built-in list data structure.
"""


class MyList(list):
    """
    MyList represents a custom version of the standard list class.
    This subclass inherits all standard behaviors and adds specific
    methods to display data in a controlled and sorted manner.
    """

    def print_sorted(self):
        """
        Public instance method that prints the current list instance
        but in an ascending sorted order. This method assumes that
        all the elements of the list will be of type integer.
        The original list instance is not modified by this method.
        """
        print(sorted(self))
