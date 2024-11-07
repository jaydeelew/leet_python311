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


# for combinations, order does not matter, e.g. we should not have duplicates [1, 2] and [2, 1]
def combinations(nums):
    def backtrack(start_index, curr_combo):
        # the if statement here prevents duplicate combos when there are duplicates in the input
        # if there were no duplicate inputs, we could just append to ans directly
        if curr_combo not in ans:
            ans.append(curr_combo[:])
            # no return statement in this context since it would prematurely ends the recursion,
            # preventing further exploration of combinations

        for i in range(start_index, len(nums)):
            curr_combo.append(nums[i])
            # we increment start_index by 1 because not doing so would result in duplicates
            # e.g. if nums = [1, 2, 3], we would get [1, 2], [2, 1], [1, 3], [3, 1],
            # [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
            # also, infinite recursion would occur since backtrack would always be called with start_index = 0
            backtrack(i + 1, curr_combo)
            curr_combo.pop()

    ans = []
    backtrack(0, [])
    return ans


ans = [1, 2, 3]
print(combinations(ans))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

ans = [1, 1, 3]  # contains duplicates
print(combinations(ans))  # Output: [[], [1], [1, 1], [1, 1, 3], [1, 3], [3]]
