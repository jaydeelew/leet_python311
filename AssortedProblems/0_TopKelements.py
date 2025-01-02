# 0. Top K Elements
# Given an array of integers, find the top k elements in arr.
import heapq


def top_k(arr, k):
    min_heap = []

    for n in arr:
        if len(min_heap) < k:
            heapq.heappush(min_heap, n)
        else:
            heapq.heappushpop(min_heap, n)

    min_heap.sort(reverse=True)
    return min_heap


arr = [3, 6, 7, 2, 9, 4]
k = 3
# Output: 9, 7, 6

print(top_k(arr, k))
