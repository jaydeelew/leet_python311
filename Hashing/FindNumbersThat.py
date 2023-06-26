# Given an integer array nums, find all the numbers x that satisfy the following:
# x + 1 is not in nums, and x - 1 is not in nums.


def find_numbers(nums):
    myset = set(nums)
    returnLlist = []
    for i in nums:
        if (i + 1 not in myset) and (i - 1 not in myset):
            returnLlist.append(i)
    return returnLlist


nums = [5, 4, 7, 2, 3, 11, 15, 14]
print(find_numbers(nums))
