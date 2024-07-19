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

    a, b = 0, 1

    for _ in range(n):
        a, b = b, a + b

    return a


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
    a, b = 0, 1
    for _ in range(n + 1):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


# iteratively return fibonacci values up through fib(n) using a generator
def fib8(n):
    a, b = 0, 1
    for _ in range(n + 1):
        yield a
        a, b = b, a + b


n = 5

print("recursive:", fib1(n))
print("memoized:", fib2(n))
print("iterative:", fib3(n))

print("recursive:", fib4(n))
print("recursive generator:", list(fib5(n)))  # generator

print("iterative:", fib6(n))
print("iterative:", fib7(n))
print("iterative generator:", list(fib7(n)))  # generator

x = fib8(n)
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())
