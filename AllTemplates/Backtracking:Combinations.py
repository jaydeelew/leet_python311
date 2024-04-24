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


# Given an array of distinct positive integer candidates and a target integer,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.


class Solution:
    def combinationSum(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr_path: list[int]):
            if len(curr_path) == len(nums):
                ans.append(curr_path[:])
                return

            for n in nums:
                curr_path.append(n)
                backtrack(curr_path)
                curr_path.pop()

        ans = []
        backtrack([])
        return ans


sol = Solution()

nums = [0, 1]
print(sol.combinationSum(nums))
# Output: [[0, 0], [0, 1], [1, 0], [1, 1]]

# nums = [1, 2, 3]
# print(sol.combinationSum(nums))
# Output: [
#     [1, 1, 1],
#     [1, 1, 2],
#     [1, 1, 3],
#     [1, 2, 1],
#     [1, 2, 2],
#     [1, 2, 3],
#     [1, 3, 1],
#     [1, 3, 2],
#     [1, 3, 3],
#     [2, 1, 1],
#     [2, 1, 2],
#     [2, 1, 3],
#     [2, 2, 1],
#     [2, 2, 2],
#     [2, 2, 3],
#     [2, 3, 1],
#     [2, 3, 2],
#     [2, 3, 3],
#     [3, 1, 1],
#     [3, 1, 2],
#     [3, 1, 3],
#     [3, 2, 1],
#     [3, 2, 2],
#     [3, 2, 3],
#     [3, 3, 1],
#     [3, 3, 2],
#     [3, 3, 3],
# ]
