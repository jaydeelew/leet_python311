# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left = runningSum = 0
        minlength = float("inf")  # set minimum length to infinity
        for right in range(len(nums)):
            runningSum += nums[right]
            while (
                runningSum >= target
            ):  # keep moving left window/subarray boundary until statement is not true
                currlength = right - left + 1
                minlength = min(
                    currlength, minlength
                )  # record shortest window with sum greater than or equal to target
                runningSum -= nums[left]
                left += 1
        # if the sum of all elements in nums[] is less than target, return 0
        return minlength if sum(nums) >= target else 0  # type: ignore


nums = [2, 3, 1, 2, 4, 3]
target = 7
# nums = [1,1,1,1,1,1,1,1]
# target = 11
sol = Solution()
print(sol.minSubArrayLen(target, nums))
