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


def combination(nums: list[int]) -> list[list[int]]:
    def backtrack(curr_path: list[int]):
        if len(curr_path) == len(nums):
            # append a copy and not a reference
            ans.append(curr_path[:])
            return

        for n in nums:
            curr_path.append(n)
            backtrack(curr_path)
            curr_path.pop()

    ans = []
    backtrack([])
    return ans


nums = [0, 1]
print(combination(nums))
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
