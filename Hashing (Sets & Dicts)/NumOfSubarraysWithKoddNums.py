# 1248. Count Number of Nice Subarrays
# Given an array of positive integers nums and an integer k.
# Find the number of subarrays with exactly k odd numbers in them.


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        counts = {}
        # this is needed for the case where 'curr - k' = 0 (if so, ans is incremented by 1)
        counts[0] = 1
        # number of times a subarray including k odds appears
        ans = 0
        # current number of odds seen as of present iteration of nums
        curr = 0

        for num in nums:
            # if current num is odd, add 1 to curr (current number of odds), else add 0
            curr += num % 2
            # if counts dictionary contains key 'curr - k', then a subarray of k odds exists
            ans += counts.get(curr - k, 0)
            # increment (or add key to counts and increment if missing) key 'curr'
            counts[curr] = counts.get(curr, 0) + 1
            # counts will end up containing all values of curr (sums of odd nums that have been added each iteration)
        return ans


nums = [1, 1, 2, 1, 1]
k = 3
# Output: 2

sol = Solution()
print(sol.numberOfSubarrays(nums, k))
