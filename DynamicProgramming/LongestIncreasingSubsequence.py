# 300. Longest Increasing Subsequence
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

from functools import cache


class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        @cache
        def dp(i):

            # Base case when dp(0)
            ans = 1

            # Recurrence Relation:
            # for each nums[j] up to but not including, nums[i],
            for j in range(i):
                # compare all nums[j] to nums[i]
                if nums[j] < nums[i]:
                    # since nums[j] is less than nums[i], call dp(j) to see if there are any other
                    # numbers that are less than nums[j] that can be added to length of subsequence
                    # maintain the current max of this subproblem dp(i)
                    ans = max(ans, dp(j) + 1)  # add 1 to the return of dp(j) for curr len of subsequence
            # return the max length subsequence
            return ans

        # return the max of all calls to dp() from dp(0) to dp(len(nums) - 1)
        return max(dp(i) for i in range(len(nums)))

    def lengthOfLIS_iter(self, nums: list[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4

# nums = [0, 1, 0, 3, 2, 3]
# Output: 4

# nums = [7, 8, 1, 2, 3]
# Output: 3

# nums = [7, 7, 7, 7, 7, 7, 7]
# Output: 1

sol = Solution()
print(sol.lengthOfLIS(nums))
print(sol.lengthOfLIS_iter(nums))
