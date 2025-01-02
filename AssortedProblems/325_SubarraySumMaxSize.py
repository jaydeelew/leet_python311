# 325. Maximum Size Subarray Sum Equals k
# Given an array nums and a target value k, find the maximum length of a subarray that sums to k.
# If there isn't one, return 0 instead.


def SubarraySum(nums, k):
    prefix_sum_dict = {}  # {prefix_sum: first_index}
    prefix_sum_dict[0] = 0
    prefix_sum = 0
    longest = 0

    for i, num in enumerate(nums, 1):
        prefix_sum += num
        check_if_prefix_sum = prefix_sum - k

        if check_if_prefix_sum in prefix_sum_dict:
            longest = max(longest, i - prefix_sum_dict[check_if_prefix_sum])

        if prefix_sum not in prefix_sum_dict:  # Only store the first occurrence
            prefix_sum_dict[prefix_sum] = i

    return longest


# nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
# k = 8
# Output: 4

nums = [1, -1, 5, -2, 3]
k = 3
# Output: 4

print(SubarraySum(nums, k))
