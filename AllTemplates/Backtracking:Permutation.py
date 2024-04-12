# def backtrack(curr, OTHER_ARGUMENTS...):
#     if (BASE_CASE):
#         # modify the answer
#         return

#     ans = 0
#     for (ITERATE_OVER_INPUT):
#         # modify the current state
#         ans += backtrack(curr, OTHER_ARGUMENTS...)
#         # undo the modification of the current state

#     return ans


# Given an array nums of distinct integers, return all the possible permutations in any order.
# For example, given nums = [1, 2, 3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]].


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr_path):
            if len(curr_path) == len(nums):
                # When adding to the answer, we need to create a copy of curr_path
                # because curr_path is only a reference to the array's address.
                ans.append(curr_path.copy())
                return

            for num in nums:
                if num not in curr_path:
                    curr_path.append(num)
                    backtrack(curr_path)
                    curr_path.pop()

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
