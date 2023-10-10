#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to reach 'n' 'H'
      characters.

    Args:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations needed to reach 'n' 'H'
          characters.

    """
    if n <= 1:
        return 0

    operations = 0
    clipboard = 1
    total = 1

    for _ in range(n):
        if n % total == 0:
            clipboard = total
            operations += 1
        operations += 1
        total += clipboard

    return operations
