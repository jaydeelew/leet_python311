# find top k elements in arr that are closest to target
import heapq


def top_k_closest_target(arr, k, target):
    max_heap = []
    for num in arr:
        dist = abs(num - target)
        if len(max_heap) < k:
            # negate the distance to make it a max heap
            heapq.heappush(max_heap, (-dist, num))
        else:
            heapq.heappushpop(max_heap, (-dist, num))

    # return the numbers in the heap and not the distances
    return [x[1] for x in max_heap]


arr = [1, 6, 7, 22, 9, 11]
k = 3
target = 5
# Output: [9, 6, 7]

print(top_k_closest_target(arr, k, target))
