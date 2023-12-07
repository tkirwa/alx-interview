#!/usr/bin/python3

"""
This module contains a function to determine the winner of a Prime Game.

The Prime Game is played by two players who take turns choosing
 a prime number from a set of consecutive integers and removing that
   number and its multiples from the set. The player who cannot make
     a move loses the game.
"""


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
    if not nums or x < 1:
        return None

    # Generate a list of prime numbers up to 10,000
    prime = [0, 0] + [1] * 9999
    p = []
    for i in range(2, 10001):
        if prime[i]:
            for j in range(i, 10001, i):
                prime[j] = i
            p.append(i)

    # Calculate the cumulative sum of primes
    cum = [0]
    for i in range(1, 10001):
        cum.append(cum[-1] + (prime[i] == i))

    # Initialize players and scores
    player = ["Maria", "Ben"]
    score = [0, 0]

    # Play the game for each round and update scores
    for n in nums:
        score[cum[n] % 2] += 1

    # Determine the winner
    if score[0] > score[1]:
        return player[0]
    elif score[0] < score[1]:
        return player[1]
    else:
        return None
