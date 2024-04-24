# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.


# def runningSum(nums):
#     prefix = [0] * len(nums)
#     prefix[0] = nums[0]

#     for i in range(1, len(nums)):
#         prefix[i] = prefix[i - 1] + nums[i]

#     return prefix


def runningSum(nums):
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    return prefix


nums = [3, 1, 2, 10, 1]
print(runningSum(nums))
# Output: [3, 4, 6, 16, 17]
