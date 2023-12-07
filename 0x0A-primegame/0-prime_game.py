#!/usr/bin/python3
def isWinner(x, nums):
    if not nums or x < 1:
        return None

    # Generate prime numbers up to max(nums)
    primes = _generate_primes(max(nums))

    # Determine the winner of each round
    Maria_score = 0
    Ben_score = 0
    for num in nums:
        winner = _play_round(num, primes)
        if winner == "Maria":
            Maria_score += 1
        elif winner == "Ben":
            Ben_score += 1

    # Determine the overall winner
    if Maria_score > Ben_score:
        return "Maria"
    elif Ben_score > Maria_score:
        return "Ben"
    else:
        return None


def _generate_primes(n):
    sieve = [True] * (n + 1)
    p = 2
    while p * p <= n:
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False
        p += 1

    primes = [p for p in range(2, n + 1) if sieve[p]]
    return primes


def _play_round(n, primes):
    game_set = set(range(1, n + 1))
    turn = "Maria"

    while game_set:
        for prime in primes:
            if prime in game_set:
                game_set -= set(range(prime, n + 1, prime))
                break
        else:
            break

        turn = "Ben" if turn == "Maria" else "Maria"

    return turn
