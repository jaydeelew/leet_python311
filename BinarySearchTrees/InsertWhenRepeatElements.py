import sys
from TextEffects import formatBinarySearch

sys.path.append("./Modules")


# If target appears multiple times, then the following will find the left-most index:
def left_insert(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        formatBinarySearch(arr, left, mid, right)
        if target <= arr[mid]:
            right = mid
        else:
            left = mid + 1

    print("For left insertion, " + str(arr[left]) + " is the insertion point\n")
    return left


# If target appears multiple times, then the following will find the right-most index:
def right_insert(arr, target):
    left = 0
    right = len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        formatBinarySearch(arr, left, mid, right)
        if target < arr[mid]:
            right = mid
        else:
            left = mid + 1

    print("For right insertion, " + str(arr[left]) + " is the insertion point\n")
    return left


arr = [1, 3, 3, 3, 3, 5, 7, 11, 15, 22, 31, 53, 62, 74, 79, 81, 82, 99, 126]
target = 3

left_insert(arr, target)
right_insert(arr, target)
