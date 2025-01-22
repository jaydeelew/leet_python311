# 0. Fibonacci
# Given an integer n, return the nth Fibonacci number.
# Implement the algorithm via bottom up iterative, top down recursive and top down recursive w/ memoization.

from Timer import Timer
from functools import cache


# decorate fib() with the cache decorator from functools library
@cache
def fib5(n):
    return n if n < 2 else fib5(n - 1) + fib5(n - 2)


# top-down recursive with built-in memoization array (or dictionary)
def fib3(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)

    return memo[n]


# botton-up iterative version
def fib1(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


# top-down recursive without memoization
def fib2(n):
    return n if n < 2 else fib2(n - 1) + fib2(n - 2)


n = 5
iterations = 1000000

t = Timer()

t.start("recursive with memoization @cache")
for _ in range(iterations):
    fib5(n)
t.stop()

t.start("recursive with built-in memoization")
for _ in range(iterations):
    fib3(n)
t.stop()

t.start("bottom up iterative")
for _ in range(iterations):
    fib1(n)
t.stop()

t.start("recursive without memoization")
for _ in range(iterations):
    fib2(n)
t.stop()
