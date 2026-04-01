#!/usr/bin/python3
"""Roman to Integer module"""


def roman_to_int(roman_string):
    """Converts a Roman numeral to an integer"""
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    res = 0
    prev = 0
    for ch in reversed(roman_string):
        curr = rom.get(ch, 0)
        if curr >= prev:
            res += curr
        else:
            res -= curr
        prev = curr
    return res
