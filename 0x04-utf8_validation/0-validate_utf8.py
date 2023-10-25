#!/usr/bin/python3
"""
This module contains a function to determine if a given data set represents
 a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Check if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list of int): List of integers representing bytes of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Check if the most significant bit is 0 (it's a one-byte character)
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                num_bytes = 0
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # Check if the current byte starts with '10'
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # Check if all characters have been validated
    return num_bytes == 0
