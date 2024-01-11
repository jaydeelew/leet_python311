# 78. Subsets
# Given an integer array nums of unique elements, return all subsets in any order without duplicates.
# For example, given nums = [1, 2, 3], return [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr, i):
            if i > len(nums):
                return

            ans.append(curr[:])
            for j in range(i, len(nums)):
                curr.append(nums[j])
                backtrack(curr, j + 1)
                curr.pop()

        ans = []
        backtrack([], 0)
        return ans


nums = [1, 2, 3]
# Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

# nums = [0]
## Output: [[], [0]]

sol = Solution()
print(sol.subsets(nums))
