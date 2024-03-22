# measure the processing time of Fibonacci algorithms:
# bottom up iterative, top down recursive, top down recursive w/ memoization

from Timer import Timer
from functools import cache, lru_cache


# top-down recursive without memoization
def fib2(n):
    if n < 2:
        return n

    return fib2(n - 1) + fib2(n - 2)


# top-down recursive with built-in memoization array (or dictionary)
def fib3(n, memo):
    # if we have already seen the result of fib(n - 1) + fib(n - 2)
    if memo[n]:  # (alternative) if memo[n] is not None:
        return memo[n]
    if n < 2:
        return n

    # here we record the result so we don't have to compute it again when seen again
    memo[n] = fib3(n - 1, memo) + fib3(n - 2, memo)
    return memo[n]


# decorate fib() with the cache decorator from functools library
@cache
def fib5(n):
    if n < 2:
        return n

    return fib5(n - 1) + fib5(n - 2)


# decorate fib() with the lru cache decorator from functools library
@lru_cache(None)
def fib6(n):
    if n < 2:
        return n

    return fib5(n - 1) + fib5(n - 2)


# botton-up iterative version
def fib1(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


n = 40
# add 1 to size of array since we need to include m[n]
# i.e. an array of size n will be indexed m[0, , , n - 1]
m = [None] * (n + 1)

t = Timer("recurive without memoization")
for _ in range(3):
    t.start()
    fib2(n)
    t.stop()

t = Timer("recursive with built-in memoization")
for _ in range(3):
    t.start()
    fib3(n, m)
    t.stop()

t = Timer("recursive with memoization @lru_cache")
for _ in range(3):
    t.start()
    fib6(n)
    t.stop()

t = Timer("bottom up iterative")
for _ in range(3):
    t.start()
    fib1(n)
    t.stop()

t = Timer("recursive with memoization @cache")
for _ in range(3):
    t.start()
    fib5(n)
    t.stop()
