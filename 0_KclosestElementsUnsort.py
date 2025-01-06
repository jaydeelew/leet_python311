# 0. Find K Closet Elements (unsorted array)
# Given an integer array arr, two integers k and target, return the k closest integers to targer in the array.
# The input array may be unsorted.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
import heapq


def findClosestElements(arr, k, target):
    max_heap = []
    for num in arr:
        dist = abs(num - target)
        if len(max_heap) < k:
            # negate the distance to make it a max heap
            # negate num as the secondary sort to follow: |a - x| == |b - x| and a < b
            heapq.heappush(max_heap, (-dist, -num))
        else:
            heapq.heappushpop(max_heap, (-dist, -num))

    # return the numbers in the heap and not the distances
    # negate the numbers again since they were negated for the secondary sort order
    return [-x[1] for x in max_heap]


arr = [9, 1, 11, 6, 22, 7]
k = 3
x = 5
# Output: [1, 7, 6]

# arr = [1, 2, 3, 4, 5]
# k = 3
# x = 3
# Output: [2, 3, 4]

print(findClosestElements(arr, k, x))
