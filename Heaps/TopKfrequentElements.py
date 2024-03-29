# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.
# It is guaranteed that the answer is unique.
from collections import Counter, deque
import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        heap = []

        # an item holds the key:value pair
        for key, val in counts.items():
            # key and val are swapped so as to order min heap by val
            heapq.heappush(heap, (val, key))
            # maintain min heap to be no greater than k so to retain k greatest values
            if len(heap) > k:
                heapq.heappop(heap)
        # need a deque so we can appendleft thereby reversing min heap pop order
        top_k_frequencies = deque()
        while heap:
            # appendleft (val, key) tuple
            top_k_frequencies.appendleft(heapq.heappop(heap))
        # entry[1] will be the key from (val, key) in top_k_frequencies
        return [entry[1] for entry in top_k_frequencies]


nums = [1, 1, 1, 2, 2, 3]
k = 2
# Output: [1,2]

# nums = [1]
# k = 1
# # Output: [1]

sol = Solution()
print(sol.topKFrequent(nums, k))
