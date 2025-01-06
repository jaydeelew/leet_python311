# 658. Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x.
# The answer should also be sorted in ascending order. If there are ties, take the smaller elements.
import heapq


class Solution:
    def findClosestElements(self, arr: list[int], k: int, x: int) -> list[int]:
        heap = []
        # difference between x and num placed into max heap
        for num in arr:
            diff = abs(num - x)
            # negate diff to maintain max heap, and num to keep lower num in a tie
            heapq.heappush(heap, (-diff, -num))
            # pop off higher diffs to maintain k-length array of lower diffs
            if len(heap) > k:
                # if more than 1 diff is same, the higher num (heap[1]) in heap will be popped first
                heapq.heappop(heap)
        # sort ascending(default) the second element in the heap tuples
        return sorted([-tuple[1] for tuple in heap])


# arr = [1, 2, 3, 4, 5]
# k = 4
# x = 3
# # Output: [1,2,3,4]

arr = [1, 2, 3, 4, 5]
k = 4
x = -1
# Output: [1,2,3,4]

sol = Solution()
print(sol.findClosestElements(arr, k, x))
