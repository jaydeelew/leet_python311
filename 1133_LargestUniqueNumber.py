# 1133. Largest Unique Number
# Given an integer array nums, return the largest integer that only occurs once.
# If no integer occurs once, return -1.

from collections import Counter


def largestUniqueNumber(nums: list[int]) -> int:
    counts = Counter(nums)
    largest = -1
    for key in counts:
        if counts[key] == 1:
            if key > largest:
                largest = key

    return largest


# nums = [2, 1, 3, 3, 1, 2]
# Output: -1

nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
# Output: 8

print(largestUniqueNumber(nums))
