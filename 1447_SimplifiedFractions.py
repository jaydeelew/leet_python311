# 1447. Simplified Fractions

# Given an integer n, return a list of all simplified fractions between 0 and 1 (exclusive)
# such that the denominator is less-than-or-equal-to n. You can return the answer in any order.


def simplifiedFractions(n: int) -> list[str]:
    simplified = []

    def gcf(a, b):
        while b:
            a, b = b, a % b
        return a

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            if gcf(i, j) == 1:
                simplified.append(str(i) + "/" + str(j))

    return simplified


# n = 2
# Output: ["1/2"]
# Explanation: "1/2" is the only unique fraction with a denominator less-than-or-equal-to 2.
# n = 3
# Output: ["1/2","1/3","2/3"]
n = 4
# Output: ["1/2","1/3","1/4","2/3","3/4"]

print(simplifiedFractions(n))
