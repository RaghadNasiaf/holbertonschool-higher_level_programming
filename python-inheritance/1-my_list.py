#!/usr/bin/python3
"""
This module contains a class MyList that inherits from the built-in list.
It provides a specialized method to print the list in a sorted manner.
"""


class MyList(list):
    """
    MyList is a subclass of the built-in list class.
    It includes an additional method for sorted display of elements.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending sorted order.
        Assumes all elements in the list are of type integer.
        """
        print(sorted(self))
