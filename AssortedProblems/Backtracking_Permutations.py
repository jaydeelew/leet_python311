# Given an array nums of distinct integers, return all the possible permutations in any order.


def permutations(nums: list[int]) -> list[list[int]]:
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


# the version uses swapping to avoid the need to check if the number is in the current path
# and uses less memory by not using a curr_path list
def permutations_2(nums):
    def bt(start):
        if start == len(nums):
            ans.append(nums[:])
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            bt(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    ans = []
    bt(0)
    return ans


# this version uses yield to avoid storing all the permutations in a list
def permutations_3(nums):
    def bt(start):
        if start == len(nums):
            # if we've reached the length of a permutation, we yield a copy of the permutation
            yield nums[:]
            return

        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            # yield from is used to yield all the permutations generated by the recursive call bt(start + 1)
            # which all come from yield nums[:]
            yield from bt(start + 1)
            nums[start], nums[i] = nums[i], nums[start]

    # we yield from bt(0) to yield all the permutations generated by bt(0)
    # which come from yield from bt(start + 1)
    # which come from yield nums[:]
    yield from bt(0)


nums = [1, 2, 3]
# Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]

# nums = [0, 1]
# # Output: [[0,1],[1,0]]

# nums = [1]
# # Output: [[1]]

print(permutations(nums))
print(permutations_2(nums))
print(list(permutations_3(nums)))
