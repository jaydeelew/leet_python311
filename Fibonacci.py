# measure the processing time of Fibonacci algorithms:
# bottom up iterative, top down recursive, top down recursive w/ memoization

from Timer import Timer
from functools import cache, lru_cache


# top-down recursive without memoization
def fib2(n):

    return n if n < 2 else fib2(n - 1) + fib2(n - 2)


# top-down recursive with built-in memoization array (or dictionary)
def fib3(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)

    return memo[n]


# decorate fib() with the cache decorator from functools library
@cache
def fib5(n):

    return n if n < 2 else fib2(n - 1) + fib2(n - 2)


# decorate fib() with the lru cache decorator from functools library
@lru_cache(None)
def fib6(n):

    return n if n < 2 else fib2(n - 1) + fib2(n - 2)


# botton-up iterative version
def fib1(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


n = 5

t = Timer()

t.start("recurive without memoization")
fib2(n)
t.stop()

t.start("recursive with built-in memoization")
fib3(n)
t.stop()

t.start("recursive with memoization @lru_cache")
fib6(n)
t.stop()

t.start("recursive with memoization @cache")
fib5(n)
t.stop()

t.start("bottom up iterative")
fib1(n)
t.stop()

t.start("bottom up iterative_2")
fib7(n)
t.stop()
