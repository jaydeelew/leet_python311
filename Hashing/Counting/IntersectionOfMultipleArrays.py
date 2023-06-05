# Example 2: 2248. Intersection of Multiple Arrays

# Given a 2D array nums that contains n arrays of distinct integers,
# return a sorted array containing all the numbers that appear in all n arrays.

# For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]],
# return [3, 4]. 3 and 4 are the only numbers that are in all arrays.

from collections import defaultdict


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        ddic = defaultdict(int)
        for array in nums:
            for i in range(len(array)):
                ddic[array[i]] += 1

        numofarrays = len(nums)
        ans = []
        for key in ddic:
            if ddic[key] == numofarrays:
                ans.append(key)
        return sorted(ans)


nums = [[7, 3, 1, 2, 4, 5], [7, 1, 2, 3, 4], [3, 4, 5, 7, 6]]
sol = Solution()
print(sol.intersection(nums))
