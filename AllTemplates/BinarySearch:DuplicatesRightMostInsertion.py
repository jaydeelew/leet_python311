# def fn(arr, target):
#     left = 0
#     right = len(arr)
#     while left < right:
#         mid = (left + right) // 2
#         if target < arr[mid]:
#             right = mid
#         else:
#             left = mid + 1
#
#     return left


def right_insert(arr, target):
    left = 0
    right = len(arr) - 1
    # cannot have left <= right as with standard binary search since infinite loop occurs if target == arr[mid]
    while left < right:
        mid = (left + right) // 2
        if target < arr[mid]:
            right = mid
        else:
            left = mid + 1

    print("\nFor right insertion, index " + str(left) + " is the insertion point\n")
    return left


arr = [1, 3, 3, 5, 7, 11, 11, 11, 15, 22]
target = 11
# Output: For right insertion, index 8 is the insertion point

right_insert(arr, target)
