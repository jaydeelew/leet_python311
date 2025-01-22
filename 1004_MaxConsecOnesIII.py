# 1004. Max Consecutive Ones III
# Given a binary array nums and an integer k,
# return the maximum number of consecutive 1's in the array if you can flip at most k 0's


def longestOnes(nums: list[int], k: int) -> int:
    left = 0
    zeros_in_window = 0  # number of flips
    max_consecutive_ones = 0

    for right in range(len(nums)):
        # If we encounter a zero, increment our zero counter
        if nums[right] == 0:
            zeros_in_window += 1

        # If we have too many zeros (flips), shrink window from left
        # until we have a valid window again.
        if zeros_in_window > k:
            # If we are removing a 0 (a flip) from the window when shrinking it,
            # decrement the amount of flips.
            if nums[left] == 0:
                zeros_in_window -= 1
            # set the beginning of the new window
            left += 1

        # Current window size is a candidate for max consecutive ones
        current_window_size = right - left + 1
        max_consecutive_ones = max(max_consecutive_ones, current_window_size)

    return max_consecutive_ones


k = 3
nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
# Output: 10

# k = 2
# nums = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1]
# # Output: 7

# k = 2
# nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
# Output: 6

print(longestOnes(nums, k))
