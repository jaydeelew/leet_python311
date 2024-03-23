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

# Given an array of positive integers nums and an integer k.
# Find the number of subarrays with exactly k odd numbers in them.
from collections import defaultdict


def subarraySum(nums: list[int], k: int) -> int:
    counter = defaultdict(int)
    # add key 0 for the case of the empty array
    counter[0] = 1
    ans = sum = 0

    for num in nums:
        # sum maintains the prefix-sum thus far
        sum += num
        # if result of sum - k already exits as key(i.e prefix-sum) in counter,
        # then we have found a subarray whose sum equals k. We add the value of that key to ans
        ans += counter[sum - k]
        # add or increment the current prefix-sum's value in the counter dictionary
        counter[sum] += 1

    return ans


nums = [1, 2, 1, 2, 1]
k = 3
# Output: 4

print(subarraySum(nums, k))
