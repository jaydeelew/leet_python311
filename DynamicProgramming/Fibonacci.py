# measure the processing time of Fibonacci algorithms:
# bottom up iterative, top down recursive, top down recursive w/ memoization
import timeit
from functools import cache, lru_cache


# botton-up iterative
def fib1(n):
    arr = [0] * (n + 1)
    arr[1] = 1
    for i in range(2, n + 1):
        arr[i] = arr[i - 1] + arr[i - 2]

    return arr[n]


# top-down recursive
def fib2(n):
    if n < 2:
        return n

    return fib2(n - 1) + fib2(n - 2)


# top-down recursive with built-in memoization
def fib3(n, memo):
    # if we have already seen the result of fib(n - 1) + fib(n - 2)
    if memo[n]:  # (alternative) if memo[n] is not None:
        return memo[n]
    if n < 2:
        return n

    # here we record the result so we don't have to compute it again when seen again
    memo[n] = fib3(n - 1, memo) + fib3(n - 2, memo)
    return memo[n]


def memoize(function):
    memo = {}

    # wrapper is the memoized function that is returned
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = function(*args)
        memo[args] = result
        return result

    return wrapper


@memoize
def fib4(n):
    if n < 2:
        return n

    return fib4(n - 1) + fib4(n - 2)


@cache
def fib5(n):
    if n < 2:
        return n

    return fib5(n - 1) + fib5(n - 2)


@lru_cache(None)
def fib6(n):
    if n < 2:
        return n

    return fib5(n - 1) + fib5(n - 2)


n = 7
# add 1 to size of array since we need to include m[n]
# i.e. an array of size n will be indexed m[0, , , n - 1]
m = [None] * (n + 1)

start = timeit.default_timer()
fib2(n)
print("recursive without memoization:", timeit.default_timer() - start)

start = timeit.default_timer()
fib3(n, m)
print("recursive with built-in memoization:", timeit.default_timer() - start)

start = timeit.default_timer()
fib4(n)
print("recursive with memoization function:", timeit.default_timer() - start)

start = timeit.default_timer()
fib5(n)
print("recursive with memoization @cache:", timeit.default_timer() - start)

start = timeit.default_timer()
fib6(n)
print("recursive with memoization @lru_cache:", timeit.default_timer() - start)

start = timeit.default_timer()
fib1(n)
print("bottom up iterative", timeit.default_timer() - start)
