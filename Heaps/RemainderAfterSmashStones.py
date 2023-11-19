# 1046. Last Stone Weight
# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# On each turn, we choose the heaviest two stones and smash them together.
# Suppose the heaviest two stones have weights x and y with x <= y.
# If x == y, then both stones are destroyed. If x != y, then x is destroyed and y loses x weight.
# Return the weight of the last remaining stone, or 0 if there are no stones left.

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        stones = [-stone for stone in stones]  # to turn min heap into max heap
        heapq.heapify(stones)  # turns an array into a heap in linear time
        while len(stones) > 1:  # while there are two or more stones
            first = abs(heapq.heappop(stones))
            second = abs(heapq.heappop(stones))
            if first != second:
                heapq.heappush(stones, -abs(first - second))  # -abs to maintain max heap

        return -stones[0] if stones else 0  # if one stone left, since it's negative, negate it


stones = [2, 7, 4, 1, 8, 1]
# Output: 1

# Input: stones = [1]
# # Output: 1

sol = Solution()
print(sol.lastStoneWeight(stones))
