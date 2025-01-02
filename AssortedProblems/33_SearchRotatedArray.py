# 33. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length)
# such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums,
# or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.


def search(nums: list[int], target: int) -> int:
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        # If the left half is sorted
        if nums[mid] >= nums[left]:
            # If the target is in the left half
            if nums[left] <= target <= nums[mid]:
                right = mid - 1
            # If the target is in the right half
            else:
                left = mid + 1
        # If the right half is sorted
        else:
            # If the target is in the right half
            if nums[mid] <= target <= nums[right]:
                left = mid + 1
            # If the target is in the left half
            else:
                right = mid - 1

    return -1


# nums = [3, 4, 5, 6, 7, 0, 1, 2]
# target = 5
# Output: 2

# nums = [4,5,6,7,0,1,2]
# target = 3
# Output: -1

# nums = [1]
# target = 0
# Output: -1

nums = [1, 3]
target = 3
# Output: 1

print(search(nums, target))
