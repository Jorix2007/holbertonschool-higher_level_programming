#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1: The first set.
        set_2: The second set.

    Returns:
        A new set containing the symmetric difference of set_1 and set_2.
    """
    # The ^ operator returns the symmetric difference of two sets
    return set_1 ^ set_2
