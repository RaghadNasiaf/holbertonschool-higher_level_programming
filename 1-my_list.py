#!/usr/bin/python3
"""
This module provides a class MyList that inherits from the list class.
"""


class MyList(list):
    """
    MyList inherits from list and includes a method to print sorted elements.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted in
        ascending order. All elements of the list are assumed to be integers.
        """
        print(sorted(self))
