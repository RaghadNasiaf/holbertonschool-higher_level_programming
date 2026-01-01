#!/usr/bin/python3
"""
This module contains a specialized list class named MyList.
The purpose of this module is to demonstrate basic inheritance by
extending the built-in list class with additional sorting functionality.
"""


class MyList(list):
    """
    MyList is a subclass that inherits all properties from the list class.
    It is designed to provide a method for displaying elements in a sorted
    fashion without affecting the original order of the list instance.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending sorted order.
        This method assumes that all elements in the list are integers.
        The original list remains unmodified after this operation.
        """
        print(sorted(self))
