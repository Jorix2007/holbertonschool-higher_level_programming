#!/usr/bin/python3
def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string: The Roman numeral string to convert.

    Returns:
        The integer value of the Roman numeral, or 0 if invalid.
    """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    total = 0
    length = len(roman_string)

    for i in range(length):
        current_val = roman_dict.get(roman_string[i], 0)

        # Wrapped the condition in parentheses to safely break the line
        if (i + 1 < length and
                current_val < roman_dict.get(roman_string[i + 1], 0)):
            total -= current_val
        else:
            total += current_val

    return total
