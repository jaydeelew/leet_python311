# 322. Coin Change
# You are given an integer array coins representing coins of different denominations and
# an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

from functools import lru_cache


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        @lru_cache(None)
        def dfs(remaining):
            # base cases
            if remaining < 0:
                return -1
            if remaining == 0:
                return 0

            min_coins = float("inf")

            for coin in coins:
                coin_count = dfs(remaining - coin)
                # coin_count of -1 occurs when dfs() is called with a negative amount
                # this difference is not considered when figuring minimum amount of coins
                if coin_count != -1:
                    min_coins = min(min_coins, coin_count + 1)
            return min_coins if min_coins != float("inf") else -1

        return dfs(amount)

    def coinChange_iter(self, coins: list[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for x in range(coin, amount + 1):
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1


coins = [5, 1, 2]
amount = 11
# Output: 3

# coins = [2]
# amount = 3
# Output: -1

# coins = [1]
# amount = 0
# Output: 0

# coins = [9, 10, 1]
# amount = 18
# Output: 2

# coins = [186, 419, 83, 408]
# amount = 6249
# Output: 20

sol = Solution()
print(sol.coinChange(coins, amount))
print(sol.coinChange_iter(coins, amount))
