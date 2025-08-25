# 78. Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
from itertools import subsets


def subsets_iterative(nums):
    ans = [[]]  # Start with empty subset

    # For each number in nums, add it to all existing subsets
    for num in nums:
        # Create new subsets by adding current number to all existing subsets
        new_subsets = []
        for subset in ans:
            new_subsets.append(subset + [num])
        ans.extend(new_subsets)

    return ans


def subsets_backtrack(nums):
    def bt(start_index, curr_combo):
        # We need a copy and not a reference
        # since we don't want the appended path(s) in ans to be modified.
        ans.append(curr_combo[:])
        # We don't want a return here since recursion would never occur
        # since there is no condition that would skip over the return statement.

        # Base case occurs when start_index equals len(nums)
        for i in range(start_index, len(nums)):
            curr_combo.append(nums[i])
            bt(i + 1, curr_combo)
            curr_combo.pop()

    ans = []
    bt(0, [])
    return ans


# nums = [1, 2]
# Output: [[], [1], [1, 2], [2]]

nums = [1, 2, 3]
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]


print(subsets_iterative(nums))
print(subsets_backtrack(nums))
