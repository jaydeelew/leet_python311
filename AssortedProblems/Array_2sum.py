# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def twoSum(nums: list[int], target: int) -> list[int]:
    num_idx = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in num_idx:
            return [i, num_idx[need]]
        num_idx[nums[i]] = i

    return []


# nums = [2, 7, 11, 15]
# target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

# nums = [3, 2, 4]
# target = 6
# Output: [1,2]

nums = [3, 3]
target = 6
# Output: [0,1]

print(twoSum(nums, target))
