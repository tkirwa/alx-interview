#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
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

    # Initialize a list to store the minimum operations for each number of
    #  characters
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = float("inf")  # Initialize to positive infinity
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n]


if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".
          format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".
          format(n, minOperations(n)))
