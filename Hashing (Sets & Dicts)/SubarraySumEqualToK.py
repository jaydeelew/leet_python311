# 560. Subarray Sum Equals K
# Given an integer array nums and an integer k, find the number of subarrays whose sum is equal to k.
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        counter = defaultdict(int)
        # add key 0 for the case of the empty array
        counter[0] = 1
        ans = sum = 0

        for num in nums:
            # sum maintains the prefix-sum thus far
            sum += num
            # if sum - k exists as key in counter, then we have found a subarray whose sum equals k
            # we add the value of that key to ans
            ans += counter[sum - k]
            # add or increment the current prefix-sum's value in the counter dictionary
            counter[sum] = counter[sum] + 1

        return ans


nums = [1, 2, 1, 2, 1]
k = 3
# Output: 4

sol = Solution()
print(sol.subarraySum(nums, k))
