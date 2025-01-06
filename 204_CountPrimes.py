# 204. Count Primes
# Given an integer n, return the number of prime numbers that are strictly less than n.


def countPrimes(n):
    if n <= 2:
        return 0

    # Start by assuming all values up to n are prime
    primes = [True] * n
    primes[0] = primes[1] = False

    # Only need to check up to square root of n
    # Any composite number larger than sqrt(n) would have been marked already
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            # Start from i*i instead of i*2
            # Numbers below i*i would have been marked by smaller prime factors
            # The [False] * len(...) part creates a list of False values of the exact length needed to fill the slice.
            primes[i * i : n : i] = [False] * len(primes[i * i : n : i])  # noqa

    return sum(primes)


n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

# n = 13
# Output: 5

# n = 0
# Output: 0

# n = 1
# Output: 0

print(countPrimes(n))
