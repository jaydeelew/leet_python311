# recursively return fib(n)
def fib1(n):

    return n if n < 2 else fib1(n - 1) + fib1(n - 2)


# recursively return fib(n) with memoization
def fib2(n, memo={0: 0, 1: 1}):

    if n not in memo:
        memo[n] = fib2(n - 1) + fib2(n - 2)

    return memo[n]


# iteratively return fib(n)
def fib3(n):
    if n < 2:
        return n

    prev, curr = 0, 1

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr


# recursively return fibonacci values up through fib(n)
def fib4(n):

    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    else:
        fib_list = fib4(n - 1)
        fib_list.append(fib_list[-1] + fib_list[-2])
        return fib_list


# recursively return fibonacci values up through fib(n) using a generator
def fib5(n):

    if n == 0:
        yield 0
    elif n == 1:
        yield 0
        yield 1
    else:
        fib_gen = fib5(n - 1)
        fib_list = list(fib_gen)
        fib_list.append(fib_list[-1] + fib_list[-2])

        for num in fib_list:
            yield num


# iteratively return fibonacci values up through fib(n)
def fib6(n):
    if n < 2:
        return [0] if n == 0 else [0, 1]
    fib_list = [0, 1]
    for i in range(2, n + 1):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list


# iteratively return fibonacci values up through fib(n)
def fib7(n):
    fib_list = []
    prev, curr = 0, 1
    for _ in range(n + 1):
        fib_list.append(prev)
        prev, curr = curr, prev + curr
    return fib_list


# iteratively return fibonacci values up through fib(n) using a generator
def fib8(n):
    prev, curr = 0, 1
    for _ in range(n + 1):
        yield prev
        prev, curr = curr, prev + curr


n = 5


print(fib1(n))
print(fib2(n))
print(fib3(n))
print(list(fib4(n)))
print(list(fib5(n)))
print(fib6(n))
print(fib7(n))
print(list(fib8(n)))
