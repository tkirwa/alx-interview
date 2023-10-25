#!/usr/bin/python3
"""
This module contains a function that checks if a given data set represents
 a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): List of integers where each integer represents
          1 byte of data.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else return False.
    """

    # Initialize count of continuation bytes
    n_bytes = 0

    # Iterate over each byte in data
    for num in data:
        # Mask the most significant 8 bits of num to get the byte
        byte = num & 0xFF

        # If no continuation bytes are expected
        if n_bytes == 0:
            # Initialize masks for checking the most significant bits of byte
            mask1 = 1 << 7
            mask2 = 1 << 6

            # Count the number of most significant bits that are 1
            while mask1 & byte:
                n_bytes += 1
                mask1 = mask1 >> 1
                mask2 = mask2 >> 1

            # If no most significant bits are 1, continue to next byte
            if n_bytes == 0:
                continue

            # If only one most significant bit is 1 or more than four most
            #  significant bits are 1, return False
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Initialize masks for checking the two most significant bits
            #  of byte
            mask1 = 1 << 7
            mask2 = 1 << 6

            # If the two most significant bits are not '10', return False
            if not (byte & mask1 and not (byte & mask2)):
                return False

            # Decrement the count of expected continuation bytes
            n_bytes -= 1

    # If all bytes are processed and no continuation byte is expected,
    #  return True
    return n_bytes == 0
