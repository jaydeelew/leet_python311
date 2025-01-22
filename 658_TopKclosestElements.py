# 658. Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x.
# The answer should also be sorted in ascending order. If there are ties, take the smaller elements.
import heapq


def findClosestElements(arr, k, x):
    heap = []
    for num in arr:
        diff = abs(num - x)
        # Negate diff to maintain max heap.
        # Negate num to keep the lower num in case more than one num has the same diff.
        heapq.heappush(heap, (-diff, -num))
        # Pop off higher diffs to maintain k-length array of lower diffs.
        if len(heap) > k:
            # If more than one diff is same, the higher num (heap[1]) in heap will be popped first.
            heapq.heappop(heap)
    # Sort ascending(default) the second element in the heap of tuples.
    return sorted([-tuple[1] for tuple in heap])


def findClosestElements2(arr, k, x):
    left = 0
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2
        # Let arr[mid] and arr[mid + k] be the boundary elements of a sliding window.
        if x - arr[mid] > arr[mid + k] - x:
            # arr[mid + k] is closer to x.
            # arr[mid] is not a candidate...
            left = mid + 1
        else:
            # arr[mid] is closer or equidistant to x.
            # arr[mid] is a candidate...
            right = mid

    return arr[left : left + k]  # noqa


arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(findClosestElements(arr, k, x))
print(findClosestElements2(arr, k, x))
# Output: [1, 2, 3, 4]

arr = [1, 2, 3, 4, 5]
k = 4
x = -1
print(findClosestElements(arr, k, x))
print(findClosestElements2(arr, k, x))
# Output: [1, 2, 3, 4]

arr = [1, 6, 7, 9, 11, 22]
k = 3
x = 10
print(findClosestElements(arr, k, x))
print(findClosestElements2(arr, k, x))

arr = [0]
k = 0
x = 0
print(findClosestElements(arr, k, x))
print(findClosestElements2(arr, k, x))
