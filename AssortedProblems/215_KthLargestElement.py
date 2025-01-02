# 215. Kth Largest Element in an Array
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
import heapq


def kth_largest(nums, k):
    heap = []
    for n in nums:
        if len(heap) < k:
            heapq.heappush(heap, n)
        else:
            heapq.heappushpop(heap, n)

    return heapq.heappop(heap)


arr = [3, 6, 7, 2, 9, 4]
k = 3
# Output: 6

print(kth_largest(arr, k))
