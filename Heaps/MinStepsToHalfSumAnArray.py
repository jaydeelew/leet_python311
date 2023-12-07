# 2208. Minimum Operations to Halve Array Sum
# You are given an array nums of positive integers.
# In one operation, you can choose any number from nums and reduce it to exactly half the number.
# Return the minimum number of operations to reduce the sum of nums by at least half.

import heapq


class Solution:
    def halveArray(self, nums: list[int]) -> int:
        target = sum(nums) / 2
        # negate each num to prepare for max heapify
        nums = [-num for num in nums]
        heapq.heapify(nums)

        num_of_ops = 0
        # if target <= 0 we have arrived at least half the sum of nums
        while target > 0:
            # num is a negative since nums is max heap
            num = heapq.heappop(nums)
            target += num / 2
            heapq.heappush(nums, num / 2)  # type: ignore
            num_of_ops += 1

        return num_of_ops


# nums = [5, 19, 8, 1]
# # Output: 3

nums = [3, 8, 20]
# Output: 3

sol = Solution()
print(sol.halveArray(nums))
