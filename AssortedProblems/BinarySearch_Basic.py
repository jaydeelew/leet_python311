# def fn(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             # do something
#             return
#         if target < arr[mid]:
#             right = mid - 1
#         else:
#             left = mid + 1

#     # left is the insertion point
#     return left


def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print("\nTarget Found\n")
            return mid
        if target < arr[mid]:
            # we want to limit our search to the left of mid
            right = mid - 1
        else:
            # we want to limit our search to the right of mid
            left = mid + 1

    print("\nTarget not found, index " + str(left) + " is the insertion point\n")
    # left is the insertion point
    return left


arr = [1, 3, 5, 7, 11, 15, 22, 31, 53, 62, 74, 79, 81, 82, 99, 126]
target = 81
# Output: Target Found

# arr = [1, 3, 5, 7, 11, 15, 22, 31, 53, 62, 74, 79, 81, 82, 99, 126]
# target = 9
# Output: Target not found, index 4 is the insertion point

binary_search(arr, target)
