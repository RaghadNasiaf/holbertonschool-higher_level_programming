#!/usr/bin/python3
"""
This module defines a specialized class that extends the standard list.
The goal is to provide additional utility methods for sorting and
displaying elements without altering the original list data.
"""


class MyList(list):
    """
    MyList is a subclass that inherits all behaviors from the list class.
    It is specifically designed to handle integer elements and provides
    a method to show them in an ascending sorted format.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending order.
        This operation uses a non-destructive approach to ensure that
        the underlying list instance remains in its original state.
        """
        print(sorted(self))
