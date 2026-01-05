#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the list base class.
It provides an additional method to print the list elements in sorted order.
"""


class MyList(list):
    """
    MyList class inherits from the built-in list class and includes
    a specific method to handle sorted printing of its elements.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted in
        ascending order. All elements of the list are assumed to be integers.
        """
        print(sorted(self))
