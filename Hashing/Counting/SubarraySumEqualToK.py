# Example 4: 560. Subarray Sum Equals K
# Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.

# from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # counts = defaultdict(int)
        counts = {}
        counts[0] = 1  # init counts with key 0 for when curr minus k equals 0 (which would be a subarray with sum of k)
        ans = curr = 0

        for num in nums:
            curr += num  # curr maintains the prefix-sum thus far
            # ans += counts[curr - k] # if curr - k has appeared before in counts, add value of that key to answer, else 0
            ans += counts.get(curr - k, 0)  # if curr - k has appeared before in counts, add value of that key to answer, else 0
            # counts[curr] += 1 # increment the current prefix-sum (key) in the counts dictionary
            counts[curr] = counts.get(curr, 0) + 1  # increment the current prefix-sum (key) in the counts dictionary

        return ans


nums = [1, 2, 1, 2, 1]
k = 3
sol = Solution()
print(sol.subarraySum(nums, k))
