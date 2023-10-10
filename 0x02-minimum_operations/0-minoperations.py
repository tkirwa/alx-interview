#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n: int) -> int:
    """
    Calculate the fewest number of operations needed to result in exactly n H
    characters in the file.

    Args:
    - n (int): The target number of characters.

    Returns:
    - int: The minimum number of operations required.

    If n is impossible to achieve, return 0.
    """
    if n <= 1:
        return 0

    op = 0
    body = 'H'
    next_char = 'H'

    for i in range(2, n + 1):
        if n % len(body) == 0:
            op += 2
            next_char = body
            body += body
        else:
            op += 1
            body += next_char

    if len(body) != n:
        return 0

    return op


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".
          format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".
          format(n, minOperations(n)))
