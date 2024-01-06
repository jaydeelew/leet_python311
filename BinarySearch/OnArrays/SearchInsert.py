# 35. Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
# You must write an algorithm with O(log n) runtime complexity.


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


# nums = [1, 3, 5, 6]
# target = 5
# # Output: 2

# nums = [1, 3, 5, 6]
# target = 2
# # Output: 1

nums = [1, 3, 5, 6]
target = 7
# Output: 4

sol = Solution()
print(sol.searchInsert(nums, target))
