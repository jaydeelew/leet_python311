# Given an array nums containing n distinct numbers in the range [0, n],
# return the only number in the range that is missing from the array.


class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        mySet = nums
        for i in range(0, len(nums) + 1):
            if i not in mySet:
                return i
        return -1


nums = [9, 6, 4, 2, 3, 5, 7, 0, 1]
sol = Solution()
print(sol.missingNumber(nums))
