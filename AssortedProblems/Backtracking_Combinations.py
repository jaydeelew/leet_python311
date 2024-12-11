# Given an array nums of distinct integers, return a list of a list of all combonations.
def combinations(nums):
    def bt(start_index, curr_combo):
        ans.append(curr_combo[:])

        for i in range(start_index, len(nums)):
            curr_combo.append(nums[i])
            if curr_combo not in ans:
                bt(i + 1, curr_combo)
            curr_combo.pop()

    ans = []
    bt(0, [])
    return ans


nums = [1, 2, 3]
# Output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]

print(combinations(nums))
