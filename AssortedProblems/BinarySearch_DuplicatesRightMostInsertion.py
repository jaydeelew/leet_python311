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


# return index of right most insertion point when duplicates are allowed
# this function will return the index just after the last duplicate,
# otherwise, the index of the next highest value
def right_insert(arr, target):
    left = 0
    right = len(arr) - 1
    # cannot have left <= right as with basic binary search
    # since infinite loop occurs if target == arr[mid]
    while left < right:
        mid = (left + right) // 2
        # If you find a match (target == arr[mid]), using < will make the algorithm
        # keep moving rightward by setting left = mid + 1.
        if target < arr[mid]:
            # we do not want to say right = mid - 1 because mid may be the insertion point
            right = mid
        else:
            left = mid + 1

    print("\nFor right insertion, index " + str(left) + " is the insertion point\n")
    return left


arr = [1, 3, 3, 5]
target = 3
# Output: For right insertion, index 3 is the insertion point

# arr = [7, 11, 22]
# target = 11
# Output: For right insertion, index 2 is the insertion point

# arr = [1, 3, 3, 5, 7, 11, 11, 11, 15, 22]
# target = 11
# Output: For right insertion, index 8 is the insertion point

right_insert(arr, target)
