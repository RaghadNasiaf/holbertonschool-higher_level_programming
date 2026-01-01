#!/usr/bin/python3
"""
This module contains a specialized class for handling list operations.
The primary objective is to demonstrate how to create a subclass that
extends the features of the standard built-in list data structure.
"""


class MyList(list):
    """
    MyList represents a custom version of the standard list class.
    This subclass inherits all behaviors from the list class and adds
    a unique method to show elements in an ascending sorted format.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending order.
        This operation ensures that the original sequence remains intact
        by using a non-destructive sorting approach on the instance.
        """
        print(sorted(self))
