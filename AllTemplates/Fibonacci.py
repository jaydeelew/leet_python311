# recursive
def fib1(n):

    return n if n < 2 else fib1(n - 1) + fib1(n - 2)


# recursive return list
def fib2(n):
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]

    fib_list = [0, 1]
    for i in range(2, n):
        fib_list.append(fib_list[i - 1] + fib_list[i - 2])

    return fib_list


# recursive wiht memoization
def fib3(n, memo={0: 0, 1: 1}):
    if n not in memo:
        memo[n] = fib3(n - 1) + fib3(n - 2)

    return memo[n]


# iterative
def fib4(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


# iterative return list
def fib5(n):
    fib_list = []
    a, b = 0, 1
    for _ in range(n):
        fib_list.append(a)
        a, b = b, a + b
    return fib_list


n = 5

print(fib1(n))
print(fib2(n))
print(fib3(n))
print(fib4(n))
print(fib5(n))
