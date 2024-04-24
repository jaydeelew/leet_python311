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
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def backtrack(starting_index, curr_path, curr_path_sum):
            # if the current path sum is equal to the target
            # append a copy of the current path to the answer
            if curr_path_sum == target:
                # append a copy and not a reference
                # if we append a reference, the current path in ans
                # will be modified when we pop from curr_path
                ans.append(curr_path[:])
                return

            for s in range(starting_index, len(candidates)):
                num = candidates[s]
                if curr_path_sum + num <= target:
                    curr_path.append(num)
                    # the starting index is s, not s+1
                    # this allows the same number to be used multiple times
                    backtrack(s, curr_path, curr_path_sum + num)
                    curr_path.pop()

        ans = []
        backtrack(0, [], 0)
        return ans


# candidates = [2]
# target = 8
# Output: [[2,2,2,2]]

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
