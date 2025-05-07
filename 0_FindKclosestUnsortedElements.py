# 0. Find K Closest Elements (unsorted array)
# Given an integer array arr, two integers k and target, return the k closest integers to targer in the array.
# The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
import heapq


def findKClosetElements(arr, k, x):
    # We negate both distance to maintainn a max heap
    # and num to pop first the lower num of equidistant nums
    # heappop() looks two next element in tuple if the previous elements are equal
    max_heap = []  # (-distance, -num)

    for num in arr:
        dist = abs(x - num)

        if len(max_heap) < k:
            heapq.heappush(max_heap, (-dist, -num))
        else:
            heapq.heappushpop(max_heap, (-dist, -num))

    # Make num positive again
    return sorted([-tup[1] for tup in max_heap])


arr = [9, 1, 11, 6, 22, 7]
k = 3
x = 5
# Output: [1, 6, 7]
print(findKClosetElements(arr, k, x))
