# 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
# For example, the array nums = [0,1,2,4,5,6,7] might become:
# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results
# in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
# Given the sorted rotated array nums of unique elements, return the minimum element of this array.
# You must write an algorithm that runs in O(log n) time.


def findMin(nums: list[int]) -> int:
    def isLessThanOrEqualToLastElement(curr: int, last: int) -> bool:
        return True if curr <= last else False

    # value of last
    last = nums[-1]
    # starting indexes of left and right
    left, right = 0, len(nums) - 1
    # current minimum
    curr_min = last

    while left <= right:
        mid = (left + right) // 2
        # same as: if arr[mid] <= arr[-1]:
        if isLessThanOrEqualToLastElement(nums[mid], last):
            curr_min = nums[mid]
            right = mid - 1
        else:
            left = mid + 1

    return curr_min


nums = [3, 4, 5, 1, 2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# nums = [4, 5, 6, 7, 0, 1, 2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.

# nums = [11, 13, 15, 17]
# Output: 11

print(findMin(nums))
