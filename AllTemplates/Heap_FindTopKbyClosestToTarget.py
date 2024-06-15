# find top k elements in arr that are closest to target
import heapq


def find_top_k_by_target_difference(arr, k, target):
    heap = []
    for num in arr:
        # negate the absolute difference to make it a max heap
        difference = -abs(num - target)
        heapq.heappush(heap, (difference, num))
        if len(heap) > k:
            heapq.heappop(heap)

    # sort heap list in descending order of the negated absolute difference
    # so that top k elements in arr are the closest to target
    heap.sort(reverse=True)
    return [num for _, num in heap]


arr = [3, 6, 7, 2, 9, 4]
k = 3
target = 5
# Output: [6, 7, 4]

print(find_top_k_by_target_difference(arr, k, target))
