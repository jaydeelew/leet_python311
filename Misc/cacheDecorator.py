from functools import cache
import time


@cache
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


start_time = time.time()
fibonacci(100)
end_time = time.time()
execution_time_without_cache = end_time - start_time
print("Time taken without cache: {:.8f} seconds".format(execution_time_without_cache))

start_time = time.time()
fibonacci(100)
end_time = time.time()
execution_time_with_cache = end_time - start_time
print("Time taken with cache: {:.8f} seconds".format(execution_time_with_cache))
