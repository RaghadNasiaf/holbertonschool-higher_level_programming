#!/usr/bin/python3
"""
This module contains a specialized list class named MyList.
The purpose of this module is to demonstrate how to inherit from the
built-in list class and add custom functionality to it.
"""


class MyList(list):
    """
    MyList is a subclass that inherits all properties from the list class.
    It provides additional methods to manipulate and display list data,
    specifically allowing for sorted output while maintaining the original.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending sorted order.
        This method assumes that all elements in the list are integers.
        It does not modify the original list instance itself.
        """
        print(sorted(self))
