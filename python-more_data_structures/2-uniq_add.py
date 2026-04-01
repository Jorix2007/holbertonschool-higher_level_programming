#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (only once for each integer).

    Args:
        my_list: The initial list of integers.

    Returns:
        The sum of all unique integers.
    """
    # Convert the list to a set to remove duplicates, then sum the elements
    return sum(set(my_list))
