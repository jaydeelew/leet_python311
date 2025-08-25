# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Integers can be negative


def subarraySumEqualsK(nums, k):
    # prefix_sum_counts maps prefix_sum -> how many times we've seen it so far.
    # A subarray ending at the current index sums to k iff (prefix_sum - k) appeared before;
    # add that frequency to the answer.
    # Seed with {0: 1} to count subarrays that start at index 0 (empty prefix).
    prefix_sum_counts = {0: 1}
    ans = prefix_sum = 0

    for num in nums:
        prefix_sum += num
        does_this_prefix_sum_exist = prefix_sum - k
        if does_this_prefix_sum_exist in prefix_sum_counts:
            # If the difference exists, it means there are subarrays ending at the current index
            # that sum to k, so we add the count of those subarrays to ans.
            ans += prefix_sum_counts[does_this_prefix_sum_exist]
        # this line must come after ans is updated or there may be an error (e.g. nums = [0], k = 0 would return 2)
        prefix_sum_counts[prefix_sum] = prefix_sum_counts.get(prefix_sum, 0) + 1
    return ans


nums = [1, 2, -1, 2, 1, -2, 3]
k = 3
# Output: 6

# nums = [1, 2, 3]
# k = 3
# Output: 2

# nums = [1, 2, 1, 2, 1]
# k = 3
# Output: 4

# nums = [0]
# k = 0
# Output: 1

# nums = []
# k = 1
# Output: 0

# nums = [1, 1, 1]
# k = 2
# Output: 2

print(subarraySumEqualsK(nums, k))
