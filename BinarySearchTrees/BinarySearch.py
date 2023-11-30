import sys

from TextEffects import banner, formatBinarySearch

sys.path.append("./Modules")


def binary_search(arr: list[int], target: int):
    left = 0
    right = len(arr) - 1
    mid = None
    while arr[left] <= arr[right]:
        mid = (left + right) // 2
        formatBinarySearch(arr, left, mid, right)
        if arr[mid] == target:
            banner("TARGET " + str(target) + " WAS FOUND!")
            return
        elif target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print("\nTarget not found but, " + str(arr[left]) + " is the insertion point\n")
    return  # return left for insertion purposes


arr = [1, 3, 5, 7, 11, 15, 22, 31, 53, 62, 74, 79, 81, 82, 99, 126]
target = 3

binary_search(arr, target)
