# You are given an integer array nums consisting of n elements, and an integer k.
# Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
# Any answer with a calculation error less than 10-5 will be accepted.


def findMaxAverage(nums, k):
    kSum = sum(nums[:k])  # sum of the first k element of nums array
    Max = d = 0  # current maximum positive adjustment to subarrays, and adjustment to subarray
    for i in range(len(nums) - k):  # loop through array indexes less than array length
        d += nums[i + k] - nums[i]  # d represents the affect on the sum of the subarry/window after shifting it to the right
        if d > Max:
            Max = d  # if d is greater than the current maximum positive adustment amount, assign the new sum to Max
    return (kSum + Max) / k
    # return (sum(nums[:k])+Max)/k


nums = [1, 12, -5, -6, 50, 3]
k = 4
print(findMaxAverage(nums, k))
