#!/usr/bin/python3
"""
0x0A. Prime Game
"""


def isWinner(x, nums):
    """
    Determines the winner of a series of checkers games.

    Args:
    - x (int): The number of rounds.
    - nums (list): An array of integers representing the range for each round.

    Returns:
    - str: The name of the player that won the most rounds.
           If the winner cannot be determined, returns None.
    """
    def is_prime(num):
        """
        Checks if a number is prime.

        Args:
        - num (int): The number to check.

        Returns:
        - bool: True if the number is prime, False otherwise.
        """
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_next_move(nums):
        """
        Finds the next prime number in the given list.

        Args:
        - nums (list): The list of integers to search.

        Returns:
        - int or None: The next prime number if found, None otherwise.
        """
        for num in nums:
            if is_prime(num):
                return num

    def remove_multiples(nums, prime):
        """
        Removes multiples of a prime number from the list.

        Args:
        - nums (list): The list of integers to filter.
        - prime (int): The prime number whose multiples should be removed.

        Returns:
        - list: The filtered list without multiples of the prime number.
        """
        return [num for num in nums if num % prime != 0]

    maria_wins = 0
    ben_wins = 0

    for round_num in range(x):
        current_nums = list(range(1, nums[round_num] + 1))

        while current_nums:
            prime = get_next_move(current_nums)
            if prime is None:
                break  # No prime numbers left to choose

            current_nums = remove_multiples(current_nums, prime)

        # Determine the winner of the current round
        if len(current_nums) % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None  # No clear winner


# Example usage
print("Winner: {}".format(isWinner(3, [4, 5, 1])))
