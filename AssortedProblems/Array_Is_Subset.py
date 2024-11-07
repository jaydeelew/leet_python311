# Given two strings, a and b, return True if a is a subset of b, otherwise return False.

from collections import Counter


def is_subset(a, b):
    status = True
    list_a = a.split()
    list_b = b.split()

    a_counter = Counter(list_a)
    b_counter = Counter(list_b)

    for num in a_counter.keys():
        if b_counter[num] and b_counter[num] >= a_counter[num]:
            b_counter[num] -= 1
        else:
            status = False

    return status


a = "3 1 9 9"
b = "5 0 7 9 4 1 3 9 6"

print(is_subset(a, b))
