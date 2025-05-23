# 46. Permutations
# Given an array of distinct integers, return all the possible permutations.
from itertools import permutations


def permutations_1(nums):
    # Most efficient solution using Python's built-in itertools module
    return list(permutations(nums))


# the version uses swapping to avoid the need to check if the number is in the current path
# and uses less memory by not using a curr_path list
def permutations_2(nums):
    # only need to check up to n - 1 since the last number will be the last one to be swapped
    def bt(start):
        if start == len(nums) - 1:
            ans.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            bt(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    ans = []
    bt(0)
    return ans


def permutations_3(nums):
    def backtrack(curr_perm):
        if len(curr_perm) == len(nums):
            # we need a copy and not a reference
            # since we don't want the appended path(s) in ans to be modified
            ans.append(curr_perm[:])
            # since there are no more numbers to add to curr_perm, we return
            return

        for num in nums:
            # we don't want to add the same number to curr_perm multiple times
            if num not in curr_perm:
                curr_perm.append(num)
                backtrack(curr_perm)
                curr_perm.pop()

    ans = []
    backtrack([])
    return ans


nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# nums = [0, 1]
# # Output: [[0,1],[1,0]]

# nums = [1]
# # Output: [[1]]

print(permutations_1(nums))
print(permutations_2(nums))
print(permutations_3(nums))
