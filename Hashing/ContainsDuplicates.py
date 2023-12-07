# 217. Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        dic = {}
        for int in nums:
            dic[int] = dic.get(int, 0) + 1
            if dic[int] > 1:
                return True
        return False


# nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] # returns True
# nums = [1, 2, 3, 4]  # returns False
nums = [1, 2, 3, 1]  # returns True

sol = Solution()
print(sol.containsDuplicate(nums))
