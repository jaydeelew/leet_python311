# Given an array of distinct integers, return a list all combinations.


def combinations(nums):
    def bt(start_index, curr_combo):
        # we need a copy and not a reference
        # since we don't want the appended path(s) in ans to be modified
        ans.append(curr_combo[:])

        for i in range(start_index, len(nums)):
            curr_combo.append(nums[i])
            bt(i + 1, curr_combo)
            curr_combo.pop()

    ans = []
    bt(0, [])
    return ans


# nums = [1, 2, 3]
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

nums = [1, 3, 1]
# Output: [[], [1], [1, 3], [1, 3, 1], [1, 1], [3]]

print(combinations(nums))
