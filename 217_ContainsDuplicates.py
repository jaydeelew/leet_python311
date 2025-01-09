# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.


def containsDuplicate(nums: list[int]) -> bool:
    return len(set(nums)) != len(nums)


# def containsDuplicate(nums: list[int]) -> bool:
#     dic = {}
#     for int in nums:
#         dic[int] = dic.get(int, 0) + 1
#         if dic[int] > 1:
#             return True
#     return False


nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]  # returns True
# nums = [1, 2, 3, 4]  # returns False
# nums = [1, 2, 3, 1]  # returns True

print(containsDuplicate(nums))
