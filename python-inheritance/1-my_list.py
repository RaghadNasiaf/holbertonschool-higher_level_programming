#!/usr/bin/python3
"""
This module defines a specialized list class named MyList.
The purpose of this module is to demonstrate how a class can inherit
all features from the built-in list class and extend its functionality
by adding custom methods for data manipulation and display.
"""


class MyList(list):
    """
    MyList is a subclass that inherits all properties from the standard list.
    This class provides a specific implementation of a list that includes
    additional utility methods, allowing users to perform operations that
    are not natively available in the basic Python list structure.
    """

    def print_sorted(self):
        """
        Public instance method that prints the list in ascending sorted order.
        This method assumes that all elements contained within the list
        instance are of type integer. It uses the built-in sorted function
        to ensure that the original list remains unmodified after display.
        """
        print(sorted(self))
