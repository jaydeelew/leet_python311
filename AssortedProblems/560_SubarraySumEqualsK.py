# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k,
# return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Integers can be negative


def subarraySumEqualsK(nums, k):
    # The prefix_sum_counts keeps track of the number of times a running sum,
    # from any index up to and including the current index, equalling k occurs.
    # The number of times a prefix-sum of 0 occurs is at least 1 for the empty list.
    # If the current prefix sum - k had been seen before in the prefix_sum_counts,
    # we add that number of times seen to the answer.
    prefix_sum_counts = {0: 1}
    ans = prefix_sum = 0

    for num in nums:
        prefix_sum += num
        check_if_prefix_sum = prefix_sum - k
        if check_if_prefix_sum in prefix_sum_counts:
            ans += prefix_sum_counts[check_if_prefix_sum]
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

print(num_of_subarrays_summing_to_k(nums, k))
