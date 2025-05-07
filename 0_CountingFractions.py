# 0. Counting Fractions
# Consider the fraction, n/d, where n and d are positive integers.
# If n < d and the only common factor is 1 (the greatest common factor(GCF), it is called a reduced proper fraction.
# If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
# 1/8, 1/7, 1/6, 1/5, 1/4,
# 2/7, 1/3, 3/8, 2/5, 3/7,
# 1/2, 4/7, 3/5, 5/8, 2/3,
# 5/7, 3/4, 4/5, 5/6, 6/7,
# 7/8
# It can be seen that there are 21 elements in this set.
# Write a program to count the number of proper fractions for a given number d.


def countFractions(d):
    def gcf(n, d):
        while d:
            n, d = d, n % d
        return n

    count = 0

    for i in range(1, d):
        for j in range(i + 1, d + 1):
            if gcf(i, j) == 1:
                count += 1

    return count


d = 8
# Output: 21

print(countFractions(d))
