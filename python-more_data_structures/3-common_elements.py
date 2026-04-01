#!/usr/bin/python3
def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        A new set containing the elements present in both sets.
    """
    # The & operator returns the intersection of two sets
    return set_1 & set_2
