# 0. Longest Subarray Sum Less Than or Equal to K
# Given an array of positive integers nums and an integer k,
# find the length of the longest subarray whose sum is less than or equal to k.


def findLongest(nums, k):
    # left boundary pointer of subarray, current sum of subarray, max length of subarray thus far
    left = curr = ans = 0
    # iterate over nums array with right boundary pointer
    for right in range(len(nums)):
        curr += nums[right]
        # while current sum is more than k (we need it less than or equal to k)
        while curr > k:
            # subtract value at left boundary pointer from current sum of current subarray
            curr -= nums[left]
            left += 1
        # maintain length of largest subarray (plus one due to zero index)
        ans = max(ans, right - left + 1)

    return ans


nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
# Output: 4

print(findLongest(nums, k))
