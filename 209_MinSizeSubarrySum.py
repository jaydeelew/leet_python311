# 209. Minimum Size Subarray Sum
# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose window_sum is greater than or equal to target. If there is no such subarray, return 0 instead.


def minSubArrayLen(target: int, nums: list[int]) -> int:
    left = window_sum = 0
    n = len(nums)
    shortest = n + 1

    for right in range(n):
        window_sum += nums[right]
        while window_sum >= target:
            shortest = min(shortest, right - left + 1)
            if shortest == 1:
                return 1
            window_sum -= nums[left]
            left += 1

    return shortest if shortest < n + 1 else 0


nums = [2, 3, 1, 2, 4, 3]
target = 7
# # Output: 2

# nums = [1, 1, 1, 1, 1, 1, 1, 1]
# target = 11
# Output: 0

print(minSubArrayLen(target, nums))
