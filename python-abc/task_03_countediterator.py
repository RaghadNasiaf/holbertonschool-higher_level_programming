#!/usr/bin/env python3
"""
Module for Task 3: Keeping track of the number of items iterated.
"""


class CountedIterator:
    """
    Iterator class that keeps track of the number of items iterated.
    """

    def __init__(self, iterable):
        """
        Initialize the iterator and a counter.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """Returns the current value of the counter."""
        return self.count

    def __next__(self):
        """
        Increments the counter and returns the next item.
        """
        try:
            item = next(self.iterator)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def __iter__(self):
        """Returns the iterator object itself."""
        return self
