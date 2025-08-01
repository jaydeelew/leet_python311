# 0. First True
# Find the first True in a sorted boolean array and return it's index.
# If there are no True elements, return -1.


def firstTrue(bools: list[bool]) -> int:
    feasible = -1
    left = 0
    right = len(bools) - 1

    while left <= right:
        mid = (left + right) // 2
        if bools[mid]:
            feasible = mid
            right = mid - 1
        else:
            left = mid + 1

    return feasible


arr = [False, False, True, True, True]
# Output: 2

# arr = [False, False, False, False, False, False, False]
# Output: -1

print(firstTrue(arr))
