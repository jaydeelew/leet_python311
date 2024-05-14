# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.


# def runningSum(nums):
#     prefix = [0] * len(nums)
#     prefix[0] = nums[0]

#     for i in range(1, len(nums)):
#         prefix[i] = prefix[i - 1] + nums[i]

#     return prefix


# with new array
def runningSum(nums):
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    return prefix


# in place
def runningSum2(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums


nums = [3, 1, 2, 10, 1]
print(runningSum(nums))
print(runningSum2(nums))
# Output: [3, 4, 6, 16, 17]
