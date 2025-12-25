#!/usr/bin/python3
"""
Roman to Integer module
"""


def roman_to_int(roman_string):
    """ Converts a Roman numeral to an integer """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0

    for i in range(len(roman_string)):
        current_val = d.get(roman_string[i], 0)
        next_val = d.get(roman_string[i + 1:i + 2], 0)
        if next_val > current_val:
            num -= current_val
        else:
            num += current_val
    return num
