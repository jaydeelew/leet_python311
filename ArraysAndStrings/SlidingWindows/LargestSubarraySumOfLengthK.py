# Example 4: Given an integer array nums and an integer k,
# find the sum of the subarray with the largest sum whose length is k.


def find_best_subarray(nums, k):
    curr = 0
    # sum the first subarray of size k
    for i in range(k):
        curr += nums[i]

    ans = curr
    for i in range(k, len(nums)):  # from k to end of nums array
        curr += (
            nums[i] - nums[i - k]
        )  # subracting leftmost element and adding rightmost element of current subarray to current sum
        ans = max(ans, curr)  # the max sum subarray thus far

    return ans


nums = [3, -1, 4, 12, -8, 5, 6]
k = 4
print(find_best_subarray(nums, k))
