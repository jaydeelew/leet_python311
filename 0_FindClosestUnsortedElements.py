# 0. Find K Closet Elements (unsorted array)
# Given an integer array arr, two integers k and target, return the k closest integers to targer in the array.
# The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
import heapq


def findClosestElements(arr, k, x):
    # Use a max heap to store the k closest elements
    # We store tuples of (-distance, value) to simulate a max heap
    heap = []

    for num in arr:
        distance = abs(num - x)
        # Build heap until while less than k
        if len(heap) < k:
            heapq.heappush(heap, (-distance, num))
        else:
            # heap[0][0] is heap[top][first element of tuple(-distance)]
            if -heap[0][0] > distance:
                heapq.heappushpop(heap, (-distance, num))

    # Extract the numbers and sort them
    result = [num for (_, num) in heap]
    result.sort()
    return result


arr = [9, 1, 11, 6, 22, 7]
k = 3
x = 5
# Output: [1, 6, 7]

print(findClosestElements(arr, k, x))
