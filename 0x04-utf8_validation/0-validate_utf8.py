#!/usr/bin/python3
"""
0-validate_utf8.py - This module contains a function to determine if a given
 data set represents  a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    This function checks if a list of integers represents a valid sequence of
      UTF-8 characters.

    Args:
    data: List of integers where each integer represents 1 byte of data.

    Returns:
    True if data is a valid UTF-8 encoding, else returns False.
    """

    # Initialize count of continuation bytes
    count = 0

    # Iterate over each byte in data
    for num in data:
        # If no continuation bytes are expected
        if count == 0:
            # Check the number of bytes the current character should take
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            # If the byte starts with '10' or '11111', it's not a
            #  valid start byte
            elif num >> 7:
                return False
        else:
            # If a continuation byte is expected, check if the byte starts
            #  with '10'
            if (num >> 6) != 0b10:
                return False
            # Decrement the count of expected continuation bytes
            count -= 1

    # If all bytes are processed and no continuation byte is expected,
    #  return True
    return count == 0
