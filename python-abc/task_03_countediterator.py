#!/usr/bin/env python3
"""
This module defines a CountedIterator class that wraps an iterable 
and tracks the number of items that have been iterated over.
"""

class CountedIterator:
    """
    A custom iterator class that extends standard iteration by maintaining a counter.
    """

    def __init__(self, iterable):
        """
        Initializes the iterator object and the counter.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def get_count(self):
        """
        Returns the current count of items that have been fetched.
        """
        return self.count

    def __next__(self):
        """
        Fetches the next item from the iterator, increments the counter, 
        and returns the item. Raises StopIteration when exhausted.
        """
        try:
            # Attempt to fetch the next item from the built-in iterator
            item = next(self.iterator)
            
            # Increment only if the fetch was successful
            self.count += 1
            
            return item
        except StopIteration:
            # Re-raise the exception when there are no more items left
            raise
