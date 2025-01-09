# 561. Array Partition
# Given an integer array nums of 2n integers,
# group these integers into n pairs (a1, b1), (a2, b2), ..., (an, bn)
# such that the sum of min(ai, bi) for all i is maximized.
# Return the maximized sum.
# e.g. nums=[1, 2, 3, 4]
# 1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
# 2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
# 3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
# So the maximum possible sum is 4.


def ArrayPairSum(nums):
    nums.sort()
    return sum(nums[::2])


nums = [1, 2, 3, 4]
# Output: 4
print(ArrayPairSum(nums))
