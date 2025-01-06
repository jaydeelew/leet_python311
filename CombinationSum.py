# 39. Combination Sum
# Given an array of distinct positive integer candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(curr_path, start, curr_path_sum):
            if curr_path_sum == target:
                # append a copy and not a reference
                ans.append(curr_path[:])
                return

            for i in range(start, len(candidates)):
                num = candidates[i]
                if curr_path_sum + num <= target:
                    curr_path.append(num)
                    # the use of i here is so that the same number from candidates can be repeated
                    # it alse does not permit evaluation of candidates less than candididates[i]
                    # because of the range of the for loop
                    backtrack(curr_path, i, curr_path_sum + num)
                    curr_path.pop()

        ans = []
        backtrack([], 0, 0)
        return ans


candidates = [2, 3, 6, 7]
target = 7
# Output: [[2,2,3],[7]]

# candidates = [2,3,5]
# target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# candidates = [2]
# target = 1
# Output: []

sol = Solution()
print(sol.combinationSum(candidates, target))
