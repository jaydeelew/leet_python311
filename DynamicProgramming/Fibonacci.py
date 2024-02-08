# measure the processing time of Fibonacci algorithms without (test1), and with (test2), memoization
import timeit


def fib1(n):
    if n == 1 or n == 2:
        return 1

    return fib1(n - 1) + fib1(n - 2)


def fib2(n, memo):
    if memo[n] is not None:
        return memo[n]

    if n == 1 or n == 2:
        return 1

    result = fib2(n - 1, memo) + fib2(n - 2, memo)
    memo[n] = result
    return result


n = 40
# add 1 to size of array since we are not using index 0
m = [None] * (n + 1)
# print(fib1(n))
# print(fib2(n, m))

start = timeit.default_timer()
fib1(n)
print("without memoization: ", timeit.default_timer() - start)

start = timeit.default_timer()
fib2(n, m)
print("with memoization: ", timeit.default_timer() - start)
