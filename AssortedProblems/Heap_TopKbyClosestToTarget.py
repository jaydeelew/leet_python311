# find top k elements in arr that are closest to target
import heapq


def find_top_k_closest_target(arr, k, target):
    max_heap = []
    for num in arr:
        # negate the absolute distance to make it a max heap
        distance = -abs(num - target)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (distance, num))
        else:
            # to maintain a heap of size k, push the new tuple, and pop the largest distance tuple
            heapq.heappushpop(max_heap, (distance, num))

    # sort the heap by the second element of the tuple (the distances)
    max_heap.sort(key=lambda x: x[1])

    # return the numbers in the heap and not the distances
    return [num for _, num in max_heap]


arr = [3, 6, 7, 2, 9, 4]
k = 3
target = 5

print(find_top_k_closest_target(arr, k, target))
