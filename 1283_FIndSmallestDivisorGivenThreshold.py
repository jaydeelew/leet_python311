# 1283. Find the Smallest Divisor Given a Threshold
# Given an array of integers nums and an integer threshold, we will choose a positive integer divisor,
# divide all the array by it, and sum the division's result.
# Find the smallest divisor such that the result mentioned above is less than or equal to threshold.
# Each result of the division is rounded to the nearest integer greater than or equal to that element.
# (For example: 7/3 = 3 and 10/2 = 5).
# The test cases are generated so that there will be an answer
import math


class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        def check(divisor):
            sum = 0
            for dividend in nums:
                sum += math.ceil(dividend / divisor)
                if sum > threshold:
                    return False

            return True

        left = 1
        # largest divisor would be equal to largest dividend
        # since smallest result would be 1 and largest the value of divisor
        right = max(nums)
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


# nums = [1, 2, 5, 9]
# threshold = 6
# # Output: 5

nums = [44, 22, 33, 11, 1]
threshold = 5

# Output: 44

sol = Solution()
print(sol.smallestDivisor(nums, threshold))
