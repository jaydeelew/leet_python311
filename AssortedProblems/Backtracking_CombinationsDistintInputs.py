# Given a list of integers, return all combinations whereby the order does not matter,
# e.g. we should not have duplicates [1, 2] and [2, 1] in the output.
from collections import Counter


# Checks if the current combination has already been seen
def same_counts(curr_ans, curr_combo):
    test_count = Counter(curr_combo)
    for combo in curr_ans:
        curr_combo_count = Counter(combo)
        if test_count == curr_combo_count:
            return True
    return False


def combinations(nums):
    def backtrack(start_index, curr_combo):
        ans.append(curr_combo[:])
        # no return statement since it would prevent the function from continuing

        for i in range(start_index, len(nums)):
            curr_combo.append(nums[i])
            # The if statement here prevents duplicate combos when there are duplicates in the input
            # if there were no duplicate inputs, we could just call bacttrack without the check.
            # Checking here instead of just before appending to ans minimizes the amount of recursive calls
            # in the case of duplicate inputs
            if same_counts(ans, curr_combo) is False:
                # we increment start_index by 1 because not doing so would result in duplicates
                # e.g. if nums = [1, 2, 3], we would get [1, 2], [2, 1], [1, 3], [3, 1],
                # [1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]
                # also, infinite recursion would occur since backtrack would always be called with start_index = 0
                backtrack(i + 1, curr_combo)
            curr_combo.pop()

    ans = []
    backtrack(0, [])
    return ans


nums = [1, 2, 3]  # contains no duplicates
print(combinations(nums))  # Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

nums = [1, 1, 3]  # contains back to back duplicates
print(combinations(nums))  # Output: [[], [1], [1, 1], [1, 1, 3], [1, 3], [3]]

nums = [1, 3, 1]  # contains duplicates not back to back
print(combinations(nums))  # Output: [[], [1], [1, 3], [1, 3, 1], [1, 1], [3], [3, 1]]
