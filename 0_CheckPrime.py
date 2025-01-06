# 0. Check Prime
# Given n, return True if n is prime, otherwise return false.


def isPrime(n):
    # Handle edge cases
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    # Only check odd numbers up to square root of n.
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


for i in range(101):
    print(f"{i} {isPrime(i)}")
