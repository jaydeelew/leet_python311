# Example 3: 713. Subarray Product Less Than K.
# Given an array of positive integers nums and an integer k,
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.

# For example, given the input nums = [10, 5, 2, 6], k = 100, the answer is 8. The subarrays with products less than k are:
# [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

# Key idea: Whenever you see a problem asking for the number of subarrays, think of this: at each index,
# how many valid subarrays end at this index?


def numSubarrayProductLessThanK(nums, k):
    if k <= 1:  # since current product cannot be 0
        return 0

    ans = left = 0  # number of contiguous subarrays
    curr = 1  # current product of subarray must be at least 1

    for right in range(len(nums)):  # iterate over array with right boundary pointer
        curr *= nums[right]  # multipy current product of subarray with next element
        while curr >= k:  # while current product of subarray is >= to k
            curr //= nums[left]  # since product of all elements in current subarray is not less that k, deduct leftmost factor
            left += 1  # move left boundary pointer forward
        ans += right - left + 1  # number of subarrays possible for this iteration of right boundary pointer added to total

    return ans


nums = [10, 5, 2, 6]
k = 100
print(numSubarrayProductLessThanK(nums, k))
