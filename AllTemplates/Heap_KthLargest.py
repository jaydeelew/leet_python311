import heapq


def kth_largest(arr: list[int], k: int) -> int:
    heap = []
    for n in arr:
        if len(heap) < k:
            heapq.heappush(heap, n)
        else:
            heapq.heappushpop(heap, n)

    return heapq.heappop(heap)


arr = [3, 6, 7, 2, 9, 4]
k = 2
# Output: 7

print(kth_largest(arr, k))
