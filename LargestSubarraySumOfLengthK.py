# Given an integer array nums and an integer k,
# find the sum of the subarray with the largest sum whose length is k.


def find_best_subarray(nums, k):
    curr = 0
    # sum the first subarray of size k
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):
        # subracting leftmost element and adding rightmost element of current subarray to current sum
        curr += nums[i] - nums[i - k]
        # the max sum subarray thus far
        ans = max(ans, curr)

    return ans


nums = [3, -1, 4, 12, -8, 5, 6]
k = 4
# Output: 18

print(find_best_subarray(nums, k))
