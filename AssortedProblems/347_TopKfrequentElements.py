# 347. Top K Frequent Elements
# Given an integer array nums and an integer k, return the k most frequent elements.
# You may return the answer in any order.
import heapq
from collections import Counter


def topKFrequent(nums, k):
    min_heap = []  # (qty, num)
    counts = Counter(nums)

    for num, qty in counts.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (qty, num))
        elif len(min_heap) >= k:
            heapq.heappushpop(min_heap, (qty, num))

    return [x[1] for x in min_heap]


# nums = [1, 1, 1, 2, 2, 3]
# k = 2
# Output: [1,2]

# nums = [1]
# k = 1
# Output: [1]

nums = [1, 2]
k = 2
# Output: [1, 2]

print(topKFrequent(nums, k))
