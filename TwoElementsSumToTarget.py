# 1. Given an array of integers nums and an integer target,
# return indices of two numbers such that they add up to target.
# You cannot use the same index twice.


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            complement = target - num
            if complement in dic:
                # return current index of nums and value from dic (complement is the key)
                return [i, dic[complement]]

            dic[num] = i

        # no two number add up to target
        return [-1, -1]


# nums = [2, 7, 11, 15]
# target = 9
# # Output: [0, 1]
# # Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

nums = [5, 2, 7, 10, 3, 9]
target = 8
# Output: [4, 0]


# nums = [3, 2, 4]
# target = 6
# # Output: [1, 2]

# nums = [3, 3]
# target = 6
# # Output: [0, 1]

sol = Solution()
print(sol.twoSum(nums, target))
