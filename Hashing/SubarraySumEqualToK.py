# 560. Subarray Sum Equals K
# Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counts = {}
        # initialize counts with key 0 for when curr minus k equals 0 (which would be a subarray with sum of k)
        counts[0] = 1
        ans = curr = 0

        for num in nums:
            # curr maintains the prefix-sum thus far
            curr += num
            # if curr - k has appeared before in counts, add value of that key to answer, else 0
            ans += counts.get(curr - k, 0)
            # increment the current prefix-sum (key) in the counts dictionary
            counts[curr] = counts.get(curr, 0) + 1

        return ans


nums = [1, 2, 1, 2, 1]
k = 3
# Output: 4

sol = Solution()
print(sol.subarraySum(nums, k))
