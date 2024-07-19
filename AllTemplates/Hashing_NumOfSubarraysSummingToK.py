# calculate the number of subarrays within nums where the sum of the elements in a subarray equals k.
def num_of_subarrays_summing_to_k(nums, k):
    # prefix_sum_count keeps track of the number of times a running sum, from any given index, equalling k occurs
    # the number of times a prefix-sum of 0 occurs is 1
    # since the empty subarray has a sum of 0.
    # also, if the current running sum is equal to k, then curr_sum - k = 0, so we have found a subarray
    # whose sum equals k, so we add 1 to the answer.
    prefix_sum_count = {0: 1}
    ans = curr_sum = 0

    for num in nums:
        curr_sum += num
        # this may or may not be an actual prefix sum
        prefix_sum = curr_sum - k
        # but if it is
        if prefix_sum in prefix_sum_count:
            ans += prefix_sum_count[prefix_sum]
        # these line must come after ans is updated or there may be an error (e.g. nums = [0], k = 0 would return 2)
        if curr_sum in prefix_sum_count:
            prefix_sum_count[curr_sum] += 1
        else:
            prefix_sum_count[curr_sum] = 1

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
