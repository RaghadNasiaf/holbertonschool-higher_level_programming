#!/usr/bin/python3
"""
This module contains the MyList class.
This class inherits from the built-in list class and provides
a method to display its elements in a sorted order.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list.
    It provides a custom method for sorted output.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list, but sorted.
        The sorting is done in ascending order and assumes integers.
        """
        print(sorted(self))
