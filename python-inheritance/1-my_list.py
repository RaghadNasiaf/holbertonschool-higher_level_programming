#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the built-in list.
It includes a method to print the elements in a sorted manner.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.
        """
        print(sorted(self))
