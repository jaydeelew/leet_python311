# 0. Is Subset
# Given two strings, a and b, return True if a is a subset of b, otherwise return False.

from collections import Counter


def is_subset(a, b):
    list_a = a.split()
    list_b = b.split()

    b_count = Counter(list_b)

    for n in list_a:
        # There is no need to test for the existence of b_count[n]
        # since the Counter object will return 0 if the key does not exist
        if b_count[n] > 0:
            b_count[n] -= 1
        else:
            return False

    return True


a = "3 1 9 9"
b = "5 0 7 9 4 1 3 9 6"
# Output: True

print(is_subset(a, b))
