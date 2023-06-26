# Example 5: 1248. Count Number of Nice Subarrays
# Given an array of positive integers nums and an integer k.
# Find the number of subarrays with exactly k odd numbers in them.

# For example, given nums = [1, 1, 2, 1, 1], k = 3, the answer is 2.
# The subarrays with 3 odd numbers in them are [1, 1, 2, 1] and [1, 2, 1, 1].

# We can check if a number is odd by taking it mod 2. If x is odd, then x % 2 = 1.


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        counts = {}
        counts[0] = 1  # this is needed for the case where 'curr - k' = 0 (if so, ans is incremented by 1)
        ans = 0  # number of times a subarray including k odds appears
        curr = 0  # current number of odds seen as of present iteration of nums

        for num in nums:
            curr += num % 2  # if current num is odd, add 1 to curr (current number of odds), else add 0
            ans += counts.get(curr - k, 0)  # if counts dictionary contains key 'curr - k', then a subarray of k odds exists
            counts[curr] = counts.get(curr, 0) + 1  # increment (or add key to counts and increment if missing) key 'curr'
            # counts will end up containing all values of curr (sums of odd nums that have been added each iteration)
        return ans


nums = [1, 1, 2, 1, 1]
k = 3
sol = Solution()
print(sol.numberOfSubarrays(nums, k))
