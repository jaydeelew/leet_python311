# 658. Find K Closest Elements
# Given a sorted integer array arr, two integers k and x,
# return the k closest integers to x in the array.
# The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:
# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b


def findClosestElements(arr, k, x):
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


# arr = [1, 6, 7, 9, 11, 22]
# k = 3
# x = 10

arr = [1, 2, 3, 4, 5]
k = 3
x = 3

print(findClosestElements(arr, k, x))
