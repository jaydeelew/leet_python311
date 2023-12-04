# 2270. Number of Ways to Split Array
# Given an integer array nums, find the number of ways to split the array into two parts so that
# the first section has a sum greater than or equal to the sum of the second section.
# The second section should have at least one number.


def waysToSplitArray(nums):
    # build a prefix array
    prefix = [nums[0]]
    for i in range(1, len(nums)):
        # add to end of prefix[] current nums element added to current last element of prefix[]
        prefix.append(nums[i] + prefix[-1])

    ans = 0
    for i in range(len(nums) - 1):
        # each element of left_section will be the sum of current left_section
        left_section = prefix[i]
        # difference between last element of prefix[] and current is sum of right_section
        right_section = prefix[-1] - prefix[i]
        if left_section >= right_section:
            ans += 1

    return ans


nums = [10, 4, -8, 7]
# Output: 2

print(waysToSplitArray(nums))
