#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the list class.
It provides a method to print the list elements in sorted order.
"""


class MyList(list):
    """
    MyList class inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted in
        ascending order. The original list is not modified.
        """
        print(sorted(self))
