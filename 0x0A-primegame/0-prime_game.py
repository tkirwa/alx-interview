#!/usr/bin/python3


def isWinner(x, nums):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    def get_primes(n):
        primes = []
        for i in range(2, n + 1):
            if is_prime(i):
                primes.append(i)
        return primes

    def play_round(n):
        primes = get_primes(n)
        turn = 0  # 0 for Maria, 1 for Ben

        while n > 0:
            current_prime = primes[0]
            primes = primes[1:]

            if turn == 0:
                n -= current_prime
            else:
                n -= current_prime * (n // current_prime)

            turn = 1 - turn

        return turn

    maria_wins = 0
    ben_wins = 0

    for i in range(x):
        winner = play_round(nums[i])
        if winner == 0:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
