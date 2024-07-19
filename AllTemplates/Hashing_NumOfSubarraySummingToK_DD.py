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


from collections import defaultdict


def num_of_subarrays_summing_to_k(nums, k):
    counts = defaultdict(int)
    counts[0] = 1
    ans = curr_sum = 0

    for num in nums:
        curr_sum += num
        ans += counts[curr_sum - k]
        counts[curr_sum] += 1

    return ans


nums = [1, 2, -1, 2, 1, -2, 3]
k = 3
# Output: 6

print(num_of_subarrays_summing_to_k(nums, k))
