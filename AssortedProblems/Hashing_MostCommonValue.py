# Given a list of numbers with duplicate values, return the most common value
from collections import Counter


def most_common_value(nums):
    counts = Counter(nums)
    # we are telling the max function to use the values of the counts dictionary as the keys for comparison
    return max(counts, key=counts.get)


nums = [1, 1, 1, 1, 2, 2, 2, 3, 3]
print(most_common_value(nums))
