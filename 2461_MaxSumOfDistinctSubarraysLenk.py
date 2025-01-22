# 2461. Maximum Sum of Distinct Subarrays With Length K
# You are given an integer array nums and an integer k.
# Find the maximum subarray sum of all the subarrays of nums that meet the following conditions:
# The length of the subarray is k, and
# All the elements of the subarray are distinct.
# Return the maximum subarray sum of all the subarrays that meet the conditions.
# If no subarray meets the conditions, return 0.
# A subarray is a contiguous non-empty sequence of elements within an array.


def find_best_subarray(nums, k):
    if k == 1:
        return max(nums)

    slow = 0
    curr_sum = nums[0]
    max_sum = float("-inf")
    last_seen = {nums[0]: 0}

    for fast in range(1, len(nums)):
        curr_sum += nums[fast]

        if nums[fast] in last_seen:
            while slow <= last_seen[nums[fast]]:
                curr_sum -= nums[slow]
                slow += 1

        last_seen[nums[fast]] = fast

        if (fast - slow + 1) > k:
            curr_sum -= nums[slow]
            slow += 1

        if (fast - slow + 1) == k:
            max_sum = max(max_sum, curr_sum)

    return max_sum if max_sum != float("-inf") else 0


nums = [1, 2, 2]
k = 2
# OUtput: 3

# nums = [1, 5, 4, 2, 9, 9, 9]
# k = 3
# Output: 15

# nums = [4, 4, 4]
# k = 3
# Output: 0

# nums = [3, -1, 4, 12, -8, 5, 6]
# k = 4
# Output: 18

# nums = [3]
# k = 1
# Output: 3

# nums = [5, 1, 3]
# k = 1
# Output: 5

# nums = [2, 5, 4, 5]
# k = 4
# Output: 0

# nums = [9, 18, 10, 13, 17, 9, 19, 2, 1, 18]
# k = 5
# Output: 68

print(find_best_subarray(nums, k))
