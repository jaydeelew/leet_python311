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
def combination_sum(candidates, target):
    def backtrack(start_index, curr_path, curr_sum):
        if curr_sum == target:
            ans.append(curr_path[:])
            # return here to avoid unnecessary adding to this path after the target is met
            return

        for i in range(start_index, len(candidates)):
            new_sum = curr_sum + candidates[i]
            # if we do not check if curr_path_sum + num <= target,
            # after the target is met the first time, the sum will keep growing as it is passed
            # to the next recursion call, and the base case will never be triggered,
            # the starting index will never be changed, and recursion will go on forever since
            # the for loop will not iterate to the next starting index
            if new_sum <= target:
                curr_path.append(candidates[i])
                # the starting index is i, not i+1
                # this allows the same number to be used multiple times per the instructions
                # if we did not make use of a starting index, we would produce duplicates (e.g. [1, 2, 2], [2, 1, 2], [2, 2, 1])
                backtrack(i, curr_path, new_sum)
                curr_path.pop()

    ans = []
    backtrack(0, [], 0)
    return ans


candidates = [1, 2, 3, 4, 5]
target = 5
# Output: [[1, 1, 1, 1, 1], [1, 1, 1, 2], [1, 1, 3], [1, 2, 2], [1, 4], [2, 3], [5]]

# candidates = [1, 2]
# target = 3
# Output: [[1,1,1],[1,2]]

# candidates = [2]
# target = 8
# Output: [[2,2,2,2]]

# candidates = [2, 3, 6, 7]
# target = 7
# Output: [[2,2,3],[7]]

# candidates = [2, 3, 5]
# target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]

# candidates = [2]
# target = 1
# Output: []

print(combination_sum(candidates, target))
