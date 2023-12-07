# 2225. You are given an integer array matches where matches[i] = [winner_i, loser_i] indicates that
# the player winner_i defeated player loser_i in a match.
# Return a list answer of size 2 where:
# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.
# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.


class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        losses_count = {}

        for winner, loser in matches:
            # if winner dne, add key w/ value 0, else value unchanged
            losses_count[winner] = losses_count.get(winner, 0)
            # if loser dne, add key w/ value 1, else increment
            losses_count[loser] = losses_count.get(loser, 0) + 1

        zero_lose, one_lose = [], []
        for player, count in losses_count.items():
            if count == 0:
                zero_lose.append(player)
            if count == 1:
                one_lose.append(player)

        return [sorted(zero_lose), sorted(one_lose)]


# matches = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]
# # Output: [[1, 2, 10], [4, 5, 7, 8]]

matches = [[2, 3], [1, 3], [5, 4], [6, 4]]
# Output: [[1, 2, 5, 6], []]

sol = Solution()
print(sol.findWinners(matches))
