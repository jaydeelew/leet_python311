# 1. Two Sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


def twoSum(nums: list[int], target: int) -> list[int]:
    num_idx = {}
    for i in range(len(nums)):
        need = target - nums[i]
        if need in num_idx:
            return [i, num_idx[need]]
        num_idx[nums[i]] = i

    return []


tests = [
    ([2, 7, 11, 15], 9, [1, 0], [0, 1], "Normal case"),
    ([3, 2, 4], 6, [1, 2], [2, 1], "Normal case"),
    ([3, 3], 6, [0, 1], [1, 0], "Duplicates"),
    ([], 1, [], [], "Empty nums list"),
    ([1], 1, [], [], "One element in list"),
    ([1, 2], 5, [], [], "Two elements not adding up to target"),
    ([1, 2], 3, [1, 0], [0, 1], "Two elements adding up to target"),
    ([1, 2, 3], 4, [0, 2], [2, 0], "First and last element adding up to target"),
]

max_len = max(len(str(test[0])) for test in tests) + 1
for input in tests:
    result = twoSum(input[0], input[1])
    print(
        f"nums: {str(input[0]):<{max_len}}"
        f"target: {str(input[1]):<3}"
        f"Expected: {str(input[2]):<6} or {str(input[3]):<8}"
        f"Result: {str(result == input[2] or result == input[3]):<7}"
        f"Desc: {input[4]}"
    )
