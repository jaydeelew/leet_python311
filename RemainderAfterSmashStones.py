# 1046. Last Stone Weight
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y.
# If x == y, then both stones are destroyed. If x != y, then x is destroyed and y loses x weight.
# Return the weight of the last remaining stone, or 0 if there are no stones left.

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # to turn min heap into max heap
        stones = [-stone for stone in stones]
        # turns an array into a heap in linear time
        heapq.heapify(stones)
        # while there are two or more stones
        while len(stones) > 1:
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                # -abs to maintain max heap
                heapq.heappush(stones, -abs(first - second))

        # if one stone left, since it's negative, negate it
        return -stones[0] if stones else 0


stones = [2, 7, 4, 1, 8, 1]
# Output: 1

# Input: stones = [1]
# # Output: 1

sol = Solution()
print(sol.lastStoneWeight(stones))
