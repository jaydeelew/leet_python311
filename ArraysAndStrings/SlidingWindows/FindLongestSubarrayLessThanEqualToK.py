# Example 1: Given an array of positive integers nums and an integer k,
# find the length of the longest subarray whose sum is less than or equal to k.


def find_length(nums, k):
    left = curr = ans = 0  # left boudary pointer of subarray, current sum of subarray, max length of subarray thus far
    for right in range(len(nums)):  # iterate over nums array with right boundary pointer
        curr += nums[right]  # add value at right boundary pointer to current sum of current subarray
        while curr > k:  # while current sum is more than k (we need it less than or equal to k)
            curr -= nums[left]  # subtract value at left boundary pointer from current sum of current subarray
            left += 1  # move left boundary pointer forward one
        ans = max(ans, right - left + 1)  # maintain length of largest subarray (plus one due to zero index)

    return ans


nums = [3, 1, 2, 7, 4, 2, 1, 1, 5]
k = 8
print(find_length(nums, k))
