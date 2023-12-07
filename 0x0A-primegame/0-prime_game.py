#!/usr/bin/python3
"""Prime game module.
"""


def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds."""
    if x < 1 or not nums:
        return None

    def can_make_move(num, remaining_numbers):
        """Check if a player can make a move in the game."""
        return any(is_prime(
            i) and i in remaining_numbers for i in range(2, num + 1))

    marias_wins, bens_wins = 0, 0

    for n in nums:
        remaining_numbers = set(range(1, n + 1))
        current_player = "Maria"

        while remaining_numbers:
            if not can_make_move(n, remaining_numbers):
                break

            valid_moves = [
                i for i in range(2, n + 1) if is_prime(
                    i) and i in remaining_numbers
            ]
            move = max(valid_moves)
            remaining_numbers -= set(range(move, n + 1, move))
            current_player = "Maria" if current_player == "Ben" else "Ben"

        if current_player == "Maria":
            marias_wins += 1
        else:
            bens_wins += 1

    if marias_wins == bens_wins:
        return None
    return "Maria" if marias_wins > bens_wins else "Ben"


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
