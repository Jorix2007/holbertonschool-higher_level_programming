#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary: The dictionary to modify.
        key: The string key to delete.

    Returns:
        The updated dictionary.
    """
    # Check if the key exists to prevent a KeyError
    if key in a_dictionary:
        del a_dictionary[key]
        
    return a_dictionary
