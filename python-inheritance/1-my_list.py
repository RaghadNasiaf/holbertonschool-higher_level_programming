#!/usr/bin/python3
"""
This module contains a specialized class for handling list operations.
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
        This public instance method displays the elements in ascending order.
        The procedure ensures that the original sequence remains intact
        by using a non-destructive sorting approach on the current instance.
        """
        print(sorted(self))
