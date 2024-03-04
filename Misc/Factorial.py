from Timer import Timer
from functools import cache


@cache
def factorial1(n):
    if n == 0 or n == 1:
        return 1

    return factorial1(n - 1) * n


def factorial2(n):
    product = 1
    for i in range(1, n + 1):
        product *= i

    return product


t = Timer("recursive")
t.start()
factorial1(500)
t.stop()

t = Timer("iterative")
t.start()
factorial2(500)
t.stop()
