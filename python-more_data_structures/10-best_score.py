#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Args:
        a_dictionary: The dictionary containing string keys and integer values.

    Returns:
        The key with the maximum value, or None if no score is found/dictionary is empty or None.
    """
    # Check if the dictionary is None or empty
    if not a_dictionary:
        return None

    # Use max() with the 'key' argument to evaluate based on dictionary values
    return max(a_dictionary, key=a_dictionary.get)
