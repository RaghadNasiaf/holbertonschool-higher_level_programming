#!/usr/bin/python3
"""
This module defines a class MyList that inherits from the list class.
It includes a method to print the list in sorted order.
"""


class MyList(list):
    """
    A class that inherits from the built-in list class.
    """

    def print_sorted(self):
        """
        Prints the list elements in ascending order without
        modifying the original list object.
        """
        sorted_list = self[:]
        sorted_list.sort()
        print(sorted_list)
