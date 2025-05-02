# 53. Maximum Subarray
# Given an integer array nums, find the subarray with the largest sum, and return its sum.


# Kadane's algorithm
def maxSubarray(nums: list[int]) -> int:
    max_sum = nums[0]
    curr_sum = 0

    for num in nums:
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += num
        max_sum = max(max_sum, curr_sum)

    return max_sum


arr = [2, 3, -8, 7, -1, 2, 3]
# Output: 11

# arr = [-2, -3, -8, -7, -1, -2, -3]
# Output: -1

print(maxSubarray(arr))
