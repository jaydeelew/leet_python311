# Example 2: 2270. Number of Ways to Split Array
# Given an integer array nums, find the number of ways to split the array into two parts so that
# the first section has a sum greater than or equal to the sum of the second section.
# The second section should have at least one number.


def waysToSplitArray(nums):
    # build a prefix array
    prefix = [nums[0]]  # array named prefix with one element which is nums[0]
    for i in range(1, len(nums)):  # from nums index 1 to index just before length of nums[]
        prefix.append(nums[i] + prefix[-1])  # add to end of prefix[] current nums element added to last element of prefix[]

    ans = 0
    for i in range(
        len(nums) - 1
    ):  # from prefix[] index 0 to second-to-last index of prefix (need to reserve last element for right side)
        left_section = prefix[i]  # each element of left_section will always be the sum of current left_section
        right_section = prefix[-1] - prefix[i]  # difference between last element of prefix[] and current is sum of right_section
        if left_section >= right_section:
            ans += 1

    return ans


nums = [10, 4, -8, 7]
print(waysToSplitArray(nums))
