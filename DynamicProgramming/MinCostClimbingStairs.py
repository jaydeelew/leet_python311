# 746. Min Cost Climbing Stars
# You are given an integer array cost where cost[i] is the cost of the ith step on a staircase.
# Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor (outside the array, not the last index of cost).


class Solution:
    # top down implementation
    def minCostClimbingStairs1(self, cost: list[int]) -> int:
        def dp(i):
            # since we call dp(i - 1), and dp(i - 2) recursively,
            # we will eventually end up at the base case when we reach steps dp(0) and dp(1)
            if i <= 1:
                # since there is no cost to reach the first two steps...
                return 0

            # make use of memoization
            if i in memo:
                return memo[i]

            # recurrence relation:
            # record and return the minumum of the previous two calls to dp
            # plus the costs of their respective steps
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]

        memo = {}
        # the length of cost is the number of steps to reach the top the stairs
        return dp(len(cost))

    # bottom up implementation (make use of top down implementation above)
    def minCostClimbingStairs2(self, cost: list[int]) -> int:
        n = len(cost)
        # in this iterative approach, dp is now an array instead of a recursive function
        # 1 is added to the array length (len of cost plus one) to allow for arrival to the top of the stairs
        dp = [0] * (n + 1)

        # base cases of dp[0] = dp[1] = 0 are implied as loop is started at 2
        # assign to dp[i] the min of previous two elements (steps) in dp, plus their corresponding costs
        for i in range(2, n + 1):
            # dp is a history of the min cost up to the ith element (dp[i])
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        # since our array is zero based, n represents the num of steps to reach top of stairs,
        # and dp[n] the min total cost to arrive
        return dp[n]


cost = [10, 15, 20]
# Output: 15

# cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
# Output: 6

sol = Solution()
print(sol.minCostClimbingStairs1(cost))
print(sol.minCostClimbingStairs2(cost))
