# You are given an integer array coins representing coins of different denominations and
# an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount.
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.


class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        if amount == 0:
            return 0
        max_coins_possible_per_coin = {}
        for i in range(len(coins)):
            max_coins_possible_per_coin[coins[i]] = amount // coins[i]

        sorted_coins = sorted(coins, reverse=True)
        result_set = set()

        for curr_denom_to_reduce in sorted_coins:
            while max_coins_possible_per_coin[curr_denom_to_reduce] > 0:
                remaining_amount = amount
                num_coins = 0
                for c in sorted_coins:
                    num_coins_denomination = max_coins_possible_per_coin[c]
                    while num_coins_denomination > 0 and remaining_amount - c >= 0:
                        remaining_amount -= c
                        num_coins_denomination -= 1
                        num_coins += 1

                if remaining_amount == 0:
                    result_set.add(num_coins)

                max_coins_possible_per_coin[curr_denom_to_reduce] -= 1

        if not result_set:
            return -1
        return min(result_set)


# coins = [1, 2, 5]
# amount = 11
# Output: 3

# coins = [2]
# amount = 3
# Output: -1

# coins = [1]
# amount = 0
# Output: 0

# coins = [1, 9, 10]
# amount = 18
# Output: 2

coins = [186, 419, 83, 408]
amount = 6249
# Output: 20

sol = Solution()
print(sol.coinChange(coins, amount))
