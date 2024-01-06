import sys
from TextEffects import formatBinarySearch

sys.path.append("./Modules")


# If target appears multiple times, return the left-most index:
def left_insert(arr, target):
    left = 0
    right = len(arr) - 1
    # cannot have left <= right as with standard binary search since infinite loop occurs if target == arr[mid]
    while left < right:
        mid = (left + right) // 2
        formatBinarySearch(arr, left, mid, right)
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1

    print("For left insertion, index " + str(left) + " is the insertion point\n")
    return left


# If target appears multiple times, return the right-most index:
def right_insert(arr, target):
    left = 0
    right = len(arr) - 1
    # cannot have left <= right as with standard binary search since infinite loop occurs if target == arr[mid]
    while left < right:
        mid = (left + right) // 2
        formatBinarySearch(arr, left, mid, right)
        if target < arr[mid]:
            right = mid
        else:
            left = mid + 1

    print("For right insertion, index " + str(left) + " is the insertion point\n")
    return left


arr = [1, 3, 3, 3, 3, 5, 7, 11, 15, 22, 31, 53, 62, 74, 79, 81, 82, 99, 126]
target = 3
# Output: For left insertion, index 1 is the insertion point
# Output: For right insertion, index 5 is the insertion point

left_insert(arr, target)
right_insert(arr, target)
