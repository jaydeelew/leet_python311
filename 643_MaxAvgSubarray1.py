# 643. Maximum Average Subarray I
# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.


def findMaxAverage(nums, k):
    # sum of the first k element of nums array
    kSum = sum(nums[:k])
    # current maximum positive adjustment to subarrays, and adjustment to subarray
    Max = d = 0
    # loop through array indexes less than array length
    for i in range(len(nums) - k):
        # d represents the affect on the sum of the subarry/window after shifting it to the right
        d += nums[i + k] - nums[i]
        # if d is greater than the current maximum positive adustment amount, assign the new sum to Max
        if d > Max:
            Max = d
    return (kSum + Max) / k


nums = [1, 12, -5, -6, 50, 3]
k = 4
# Output: 8

print(findMaxAverage(nums, k))
