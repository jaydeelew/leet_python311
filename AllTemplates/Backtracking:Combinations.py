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


# for combinations, order does not matter (eg. [1, 2] and [2, 1] are considered the same)
def combinations(nums):
    def backtrack(start_index, curr_combo):
        # no if statement here because we are appending all the combinations
        ans.append(curr_combo[:])

        for i in range(start_index, len(nums)):
            curr_combo.append(nums[i])
            backtrack(i + 1, curr_combo)
            curr_combo.pop()

    ans = []
    backtrack(0, [])
    return ans


ans = [1, 2, 3]
print(combinations(ans))
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
