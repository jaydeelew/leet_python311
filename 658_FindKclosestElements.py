# 658. Find K Closest Elements
# Given a sorted integer array arr, two integers k and x, return the k closest integers to x.
# The answer should also be sorted in ascending order. If there are ties, take the smaller elements.


def findKClosestElements(arr, k, x):
    left = 0
    # We subtract k from len(arr) to keep our window's begining far enough
    # left to prevent the right boundary from going passed the array.
    right = len(arr) - k

    while left < right:
        mid = (left + right) // 2
        # Let arr[mid] and arr[mid + k] be the boundary elements of a sliding window.
        if x - arr[mid] > arr[mid + k] - x:
            # Right boundary, arr[mid + k], is closer to x than arr[mid]
            # Move window right and don't include arr[mid]
            left = mid + 1
        else:
            # Left boundary, arr[mid], is closer or equidistant to x than arr[mid + k]
            # Move window left and include arr[mid] because when the two boundaries are equidistant,
            # we choose the smaller of the two boundary elements.
            right = mid

    return arr[left : left + k]  # noqa


arr = [0, 1, 2, 3, 4, 5, 6]
k = 4
x = 3
print(findKClosestElements(arr, k, x))
# Output: [2, 3, 4, 5]

# arr = [1, 2, 3, 4, 5]
# k = 4
# x = 2
# print(findKClosestElements(arr, k, x))
# # Output: [1, 2, 3, 4]

# arr = [1, 5, 7, 9, 11, 22]
# k = 3
# x = 10
# print(findKClosestElements(arr, k, x))
# # Output: [7, 9, 11]

# arr = [1, 5, 7, 9, 11, 22]
# k = 3
# x = 7
# print(findKClosestElements(arr, k, x))
# # Output: [5, 7, 9]

# arr = [0]
# k = 0
# x = 0
# print(findKClosestElements(arr, k, x))
# # Output: []
