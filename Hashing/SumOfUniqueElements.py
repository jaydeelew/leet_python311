# You are given an integer array nums.
# The unique elements of an array are the elements that appear exactly once in the array.
# Return the sum of all the unique elements of nums.

from collections import Counter


class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        numsCounter = Counter(nums)
        sum = 0
        for key in numsCounter:
            if numsCounter[key] == 1:
                sum += key
        return sum


nums = [1, 2, 3, 2]  # returns 4
# nums = [1, 1, 1, 1, 1]  # returns 0
sol = Solution()
print(sol.sumOfUnique(nums))
