# Given a sorted array of unique integers and a target integer,
# return true if there exists a pair of numbers that sum to target, false otherwise.
# This problem is similar to Two Sum.


def check_for_target(nums, target):
    left = 0
    right = len(nums) - 1

    while left < right:
        curr = nums[left] + nums[right]
        if curr == target:
            return True
        if curr > target:
            right -= 1
        else:
            left += 1

    return False


nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
# Output: True

print(check_for_target(nums, target))
