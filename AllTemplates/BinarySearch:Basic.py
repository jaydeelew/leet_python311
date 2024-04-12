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


def binary_search(arr: list[int], target: int):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print("\nTarget Found\n")
            return
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    print("\nTarget not found, " + str(arr[left]) + " is the insertion point\n")
    return  # or return left for insertion purposes


arr = [1, 3, 5, 7, 11, 15, 22, 31, 53, 62, 74, 79, 81, 82, 99, 126]

target = 81
# Output: Target Found

# target = 9
# Output: Target not found but, 11 is the insertion point

binary_search(arr, target)
