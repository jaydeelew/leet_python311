# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
from itertools import combinations


def subsets_1(nums):
    result = [[]]  # Empty set is always part of the power set
    for i in range(1, len(nums) + 1):
        # For each length i, get all combinations of length i
        result.extend(list(combinations(nums, i)))
    return result


def subsets_2(nums):
    n = len(nums)
    # Total number of subsets for n elements is 2^n
    total_subsets = 1 << n
    result = []

    for i in range(total_subsets):
        # Each number from 0 to 2^n-1 represents a subset
        subset = []
        for j in range(n):
            # Check if jth bit is set in i
            if (i & (1 << j)) > 0:
                subset.append(nums[j])
        result.append(subset)

    return result


def subsets_3(nums):
    def bt(start_index, curr_combo):
        # We need a copy and not a reference
        # since we don't want the appended path(s) in ans to be modified.
        ans.append(curr_combo[:])
        # We don't want to return here since recursion would never occur
        # since there is no condition that would skip over the return statement.

        # Base case occurs when start_index equals len(nums)
        for i in range(start_index, len(nums)):
            curr_combo.append(nums[i])
            bt(i + 1, curr_combo)
            curr_combo.pop()

    ans = []
    bt(0, [])
    return ans


nums = [1, 2]
# Output: [[], [1], [1, 2], [2]]

# nums = [1, 2, 3]
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

print(subsets_1(nums))
print(subsets_2(nums))
print(subsets_3(nums))
