# 1962. You are given a 0-indexed integer array piles, where piles[i] represents the number of stones in the ith pile,
# and an integer k. You should apply the following operation exactly k times:
# Choose any piles[i] and remove floor(piles[i] / 2) stones from it.
# Notice that you can apply the operation on the same pile more than once.
# Return the minimum possible total number of stones remaining after applying the k operations.
# floor(x) is the greatest integer that is smaller than or equal to x (i.e., rounds x down).
import heapq
from math import floor


class Solution:
    def minStoneSum(self, piles: list[int], k: int) -> int:
        piles = [-p for p in piles]
        heapq.heapify(piles)

        for _ in range(k):
            # floor of negative number rounds down as well: floor(-2.5) == 3
            split_stone = -floor(heapq.heappop(piles) / 2)
            heapq.heappush(piles, -split_stone)

        return -sum(piles)


piles = [5, 4, 9]
k = 2
# Output: 12

sol = Solution()
print(sol.minStoneSum(piles, k))
