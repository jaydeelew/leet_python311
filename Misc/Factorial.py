def factorial1(n):
    if n == 0 or n == 1:
        return 1

    return factorial1(n - 1) * n


def factorial2(n):
    product = 1
    for i in range(1, n + 1):
        product *= i

    return product


print(factorial1(10))
print(factorial2(10))
