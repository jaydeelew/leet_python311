# calculate the number of subarrays within nums where the sum of the elements in a subarray equals k.
from collections import defaultdict


def num_of_subarrays_summing_to_k(nums, k):
    # prefix_sum_count keeps track of the number of times a running sum, from any given index, equalling k occurs
    # the number of times a prefix-sum of 0 occurs is at least 1 for the empty list
    # if the current running sum is equal to k, then curr_sum - k = 0, so we have found a subarray
    # whose sum equals k, we add 1 to the answer.
    prefix_sum_count = defaultdict(int)
    prefix_sum_count[0] = 1
    ans = running_sum = 0

    for num in nums:
        running_sum += num
        prefix_sum_check = running_sum - k
        if prefix_sum_check in prefix_sum_count:
            ans += prefix_sum_count[prefix_sum_check]
        # this line must come after ans is updated or there may be an error (e.g. nums = [0], k = 0 would return 2)
        prefix_sum_count[running_sum] += 1
    return ans


# nums = [1, 2, -1, 2, 1, -2, 3]
# k = 3
# Output: 6

nums = [1, 2, 3]
k = 3
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
