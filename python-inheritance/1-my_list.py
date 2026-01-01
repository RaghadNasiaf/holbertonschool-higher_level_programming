#!/usr/bin/python3
"""
Module documentation for MyList class.
This module provides a class that inherits from list and adds sorting.
"""


class MyList(list):
    """
    Class documentation for MyList.
    Inherits from list and provides a method to print sorted elements.
    """

    def print_sorted(self):
        """
        Method documentation for print_sorted.
        Prints the list elements in ascending order.
        """
        print(sorted(self))
