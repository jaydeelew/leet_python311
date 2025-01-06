# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = runningSum = 0
        minlength = float("inf")
        for right in range(len(nums)):
            runningSum += nums[right]
            # keep moving left window/subarray boundary until statement is not true
            while runningSum >= target:
                currlength = right - left + 1
                # record shortest window with sum greater than or equal to target
                minlength = min(currlength, minlength)
                runningSum -= nums[left]
                left += 1
        # if the sum of all elements in nums[] is less than target, return 0
        return minlength if sum(nums) >= target else 0  # type: ignore


# nums = [2, 3, 1, 2, 4, 3]
# target = 7
# # Output: 2

nums = [1, 1, 1, 1, 1, 1, 1, 1]
target = 11
# Output: 0

sol = Solution()
print(sol.minSubArrayLen(target, nums))
