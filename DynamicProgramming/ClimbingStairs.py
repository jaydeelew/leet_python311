# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

from functools import cache


class Solution:
    # top down
    def climbStairs(self, n: int) -> int:
        @cache
        def dp(step):
            num_ways = 0

            # base cases
            if step == 1:
                return 1
            if step == 2:
                return 2

            # recurrence relation
            num_ways += dp(step - 2) + dp(step - 1)

            return num_ways

        return dp(n)

    # bottom up
    def climbStairs_iter(self, n: int) -> int:
        if n < 3:
            return n

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2

        for step in range(2, n):
            dp[step] = dp[step - 2] + dp[step - 1]

        return dp[-1]


# n = 2
# Output: 2

n = 3
# Output: 3

sol = Solution()
print(sol.climbStairs(n))
print(sol.climbStairs_iter(n))
