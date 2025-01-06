# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.


def sortedSquares(nums):
    ans = [0] * len(nums)
    left = 0
    right = len(nums) - 1

    # range starts from end. Second -1 is end of range and not included for i
    for i in range(len(nums) - 1, -1, -1):
        if abs(nums[left]) >= abs(nums[right]):
            square = nums[left]
            left += 1
        else:
            square = nums[right]
            right -= 1
        ans[i] = square * square

    return ans


nums = [-7, -3, -1, 0, 3, 11]
# Output: [0, 1, 9, 9, 49, 121]

print(sortedSquares(nums))
