# Create function that takes an integer, num, and returns a list a list of prime numbers up to and including num.


def primes(num):
    ans = []
    if num < 2:
        return []
    for i in range(2, num + 1):
        isPrime = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                isPrime = False
        if isPrime == True:
            ans.append(i)

    return ans


print(primes(19))
