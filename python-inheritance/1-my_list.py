#!/usr/bin/python3
"""
This module provides a specialized list class named MyList.
The MyList class inherits all functionalities from the built-in list class
and adds a unique feature to display elements in a specific sorted order.
"""


class MyList(list):
    """
    MyList is a subclass that extends the standard Python list.
    This class is designed to demonstrate basic inheritance concepts
    by adding a custom method to the existing list data structure.
    """

    def print_sorted(self):
        """
        This method prints the elements of the list in ascending sorted order.
        It assumes that all elements within the list are of integer type.
        The method uses the sorted function to ensure the original list
        remains unmodified after the printing operation.
        """
        print(sorted(self))
