# 0. Lefmost Insert
# Given a sorted array, return index of leftmost insertion point when duplicates are allowed


def leftMostInsert(arr, target):
    left = 0
    right = len(arr) - 1
    # cannot have while left <= right as with basic binary search
    # since infinite loop occurs if target == arr[mid]
    while left < right:
        mid = (left + right) // 2
        # If you find a match (target == arr[mid]), using <= will make the algorithm
        # keep moving leftward by setting right = mid
        if target <= arr[mid]:
            # We do not want to say right = mid - 1 because mid may be the insertion point
            right = mid
        else:
            left = mid + 1

    print("\nFor left insertion, index " + str(left) + " is the insertion point\n")
    return left


arr = [1, 3, 3, 5]
target = 3
# Output: For left insertion, index 1 is the insertion point

# arr = [7, 11, 22]
# target = 11
# Output: For left insertion, index 1 is the insertion point

# arr = [1, 3, 3, 5, 7, 11, 11, 11, 15, 22]
# target = 11
# Output: For left insertion, index 5 is the insertion point

leftMostInsert(arr, target)
