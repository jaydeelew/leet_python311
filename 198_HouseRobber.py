# 198. House Robber
# You are planning to rob houses along a street. The ith house has nums[i] money.
# If you rob two houses beside each other, the alarm system will trigger and alert the police.
# What is the most money you can rob without alerting the police?


class Solution:
    # top down implementation of dynamic programming
    def rob(self, nums: list[int]) -> int:
        def dp(index):
            # two base cases are needed:
            if index == 0:
                # if we are at the first house
                return nums[0]
            if index == 1:
                # if we are at the second house
                return max(nums[0], nums[1])

            # make use of memoization
            if index in memo:
                return memo[index]

            # recurrence relation:
            # save in memmo and return max money of going with previouse house,
            # or with the house before previous plus current one
            memo[index] = max(dp(index - 1), dp(index - 2) + nums[index])
            return memo[index]

        memo = {}
        # pass the index of the last element in nums
        return dp(len(nums) - 1)

    # bottom up iterative approach
    def rob2(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for index in range(2, len(nums)):
            dp[index] = max(dp[index - 1], dp[index - 2] + nums[index])

        return dp[-1]

    # bottom up iteractive approach without dp array for O(1) space complexity
    def rob3(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        back_two = nums[0]
        back_one = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # back_two becomes back_one, and back_one gets updated
            back_one, back_two = max(back_one, back_two + nums[i]), back_one

        return back_one


# nums = [1, 2, 3, 1]
# Output: 4

nums = [2, 7, 9, 3, 1]
# Output: 12

# nums = [5, 2]
# Output = 5

# nums = [1]
# Output: 1

sol = Solution()
print(sol.rob(nums))
print(sol.rob2(nums))
print(sol.rob3(nums))
