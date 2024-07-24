import heapq


def kth_largest(nums, k):
    # This function maintains a min-heap of size k. It uses heappushpop for optimal efficiency.
    heap = []
    for n in nums:
        if len(heap) < k:
            heapq.heappush(heap, n)
        else:
            heapq.heappushpop(heap, n)

    return heapq.heappop(heap)


def kth_largest_2(nums, k):
    # This function maintains a min-heap and allows it to grow to k+1 before popping the smallest element.
    heap = []
    for n in nums:
        heapq.heappush(heap, n)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


arr = [3, 6, 7, 2, 9, 4]
k = 2
# Output: 7

print(kth_largest(arr, k))
print(kth_largest_2(arr, k))
