# 46. Permutations
# Given an array nums of distinct integers, return all the possible permutations in any order.
# For example, given nums = [1, 2, 3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr):
            if len(curr) == len(nums):
                # When adding to the answer, we need to create a copy of curr
                # because curr is only a reference to the array's address.
                ans.append(curr.copy())
                return

            for num in nums:
                if num not in curr:
                    curr.append(num)
                    backtrack(curr)
                    # pop last appended value so we have len(nums) new calls to backtrack
                    # each with curr adding one additional element
                    # e.g. the iteration of nums = [1, 2, 3] will call backtrack([1]), backtrack([2]), bactrack([3])
                    curr.pop()

        ans = []
        backtrack([])
        return ans


nums = [1, 2, 3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

# nums = [0,1]
# # Output: [[0,1],[1,0]]

# nums = [1]
# # Output: [[1]]

sol = Solution()
print(sol.permute(nums))
