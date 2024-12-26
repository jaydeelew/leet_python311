# 704. Binary Search
# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.


def binary_search(arr: list[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if target < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


arr = [1, 3, 5, 7, 11, 15, 22, 31, 53, 62, 74, 79, 81, 82, 99, 126]
target = 81
# Output: 81

# arr = [1, 3, 5, 7, 11, 15, 22, 31, 53, 62, 74, 79, 81, 82, 99, 126]
# target = 9
# Output: -1

print(binary_search(arr, target))
