#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary: The dictionary to update.
        key: The string key to add or update.
        value: The value to associate with the key.

    Returns:
        The updated dictionary.
    """
    # This single line handles both creation and replacement
    a_dictionary[key] = value
    return a_dictionary
