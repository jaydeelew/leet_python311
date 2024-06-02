# from collections import defaultdict

# def fn(arr, k):
#     counts = defaultdict(int)
#     counts[0] = 1
#     ans = curr = 0

#     for num in arr:
#         # do logic to change curr
#         ans += counts[curr - k]
#         counts[curr] += 1

#     return ans

# calculates the number of subarrays within the given list nums where
# the sum of the elements in the subarray equals the integer k.


from collections import defaultdict


# calculates the current prefix sum and checks if the difference between the current prefix sum
# and the target sum k has been seen before.
# If it has, we have found a subarray whose sum equals k,
# so we add the count of that difference (from the hashmap) to the answer
def num_of_subarrays_summing_to_k(nums, k):
    # prefix_sum_count keeps track of the number of times a running sum, from any given index, equalling k occurs
    prefix_sum_count = defaultdict(int)
    # the number of times a prefix-sum of 0 occurs is 1,
    # since the empty subarray has a sum of 0
    # also if the current running sum is equal to k, then curr_sum - k = 0, so we have found a subarray
    # whose sum equals k, so we add 1 to the answer
    prefix_sum_count[0] = 1
    curr_sum = 0
    ans = 0

    for num in nums:
        # curr_sum maintains the prefix-sum/running-sum thus far
        curr_sum += num
        # if curr_sum - k exists in prefix_sum_count, then we have found a subarray
        # whose sum equals k, so we add the count of that difference (from the hashmap) to the answer
        ans += prefix_sum_count[curr_sum - k]
        # this line must come after ans is updated or there may be an error (eg nums = [0], k = 0 would return 2)
        prefix_sum_count[curr_sum] += 1

    return ans


nums = [1, 2, 3, 4, 5]
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

print(num_of_subarrays_summing_to_k(nums, k))
