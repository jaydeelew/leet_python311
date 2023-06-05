# Example 2: Given a sorted array of unique integers and a target integer,
# return true if there exists a pair of numbers that sum to target, false otherwise.
# This problem is similar to Two Sum.

# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, return true because 4 + 9 = 13.


def check_for_target(nums, target):
    left = 0  # left boundary pointer
    right = len(nums) - 1  # right boundary pointer

    while left < right:
        curr = nums[left] + nums[right]  # current sum of left and right boundary pointers
        if curr == target:  # if current sum equals target
            return True
        if curr > target:  # if current sum is greater than target
            right -= 1  # move right boundary pointer toward the center
        else:
            left += 1  # move left boundary pointer toward the center

    return False  # if target not found


nums = [1, 2, 4, 6, 8, 9, 14, 15]
target = 13
print(check_for_target(nums, target))
