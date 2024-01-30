# 78. Subsets
# Given an integer array nums of unique elements, return all subsets in any order without duplicates.


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def backtrack(curr_path, i):
            # a base case is not necessary here since the for loop terminates at length of nums
            # and backtrack is no longer called.

            # for each call to this recursive function, append a copy of curr_path (e.g. curr_path[:]) to ans[]
            # and not the reference to curr_path since a reference to curr_path (e.g. curr_path) in ans[] will keep changing
            ans.append(curr_path.copy())

            for j in range(i, len(nums)):
                curr_path.append(nums[j])
                backtrack(curr_path, j + 1)
                curr_path.pop()

        ans = []
        backtrack([], 0)
        return ans


nums = [1, 2, 3]
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

# nums = [0]
# # Output: [[], [0]]

sol = Solution()
print(sol.subsets(nums))
