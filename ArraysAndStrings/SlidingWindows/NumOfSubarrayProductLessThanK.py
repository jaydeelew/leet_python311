# 713. Subarray Product Less Than K.
# Given an array of positive integers nums and an integer k,
# return the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than k.
# Key idea: Whenever you see a problem asking for the number of subarrays, think of this: at each index,
# how many valid subarrays end at this index?


def numSubarrayProductLessThanK(nums, k):
    # since current product cannot be 0
    if k <= 1:
        return 0

    # number of contiguous subarrays
    ans = left = 0
    # current product of subarray must be at least 1
    curr = 1

    # iterate over array with right boundary pointer
    for right in range(len(nums)):
        # multipy current product of subarray with next element
        curr *= nums[right]
        # while current product of subarray is >= to k
        while curr >= k:
            # since product of all elements in current subarray is not less that k, deduct leftmost factor
            curr //= nums[left]
            left += 1
        # number of subarrays possible for this iteration of right boundary pointer added to total
        ans += right - left + 1

    return ans


nums = [10, 5, 2, 6]
k = 100
# Output: 8
# The subarrays with products less than k are: [10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]

print(numSubarrayProductLessThanK(nums, k))
