#!/usr/bin/python3

"""
This module contains a function to determine the winner of a Prime Game.

The Prime Game is played by two players who take turns choosing a prime
 number from a set of consecutive integers and removing that number and
   its multiples from the set. The player who cannot make a move loses
     the game.
"""


def is_prime(num):
    """
    Check if a number is prime.

    Parameters:
    num (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def get_primes_up_to_n(n):
    """
    Get a list of prime numbers up to n.

    Parameters:
    n (int): The maximum number to check for primality.

    Returns:
    list: A list of prime numbers up to n.
    """
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes


def isWinner(x, nums):
    """
    Determine the winner of the Prime Game.

    Parameters:
    x (int): The number of rounds.
    nums (list): A list of integers representing the maximum number
      in each round.

    Returns:
    str: The name of the player who won the most rounds, or None if there
      is a tie.
    """
    wins = {"Maria": 0, "Ben": 0}

    for n in nums:
        primes = get_primes_up_to_n(n)
        remaining_numbers = set(range(1, n + 1))

        current_player = "Maria"

        while remaining_numbers:
            valid_moves = [p for p in primes if p in remaining_numbers]
            if not valid_moves:
                break

            move = max(valid_moves)
            remaining_numbers -= set(range(move, n + 1, move))
            current_player = "Maria" if current_player == "Ben" else "Ben"

        if current_player == "Maria":
            wins["Maria"] += 1
        else:
            wins["Ben"] += 1

    if wins["Maria"] > wins["Ben"]:
        return "Maria"
    elif wins["Ben"] > wins["Maria"]:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
