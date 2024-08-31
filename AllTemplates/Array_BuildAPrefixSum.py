# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.


# def runningSum(nums):
#     prefix = [0] * len(nums)
#     prefix[0] = nums[0]

#     for i in range(1, len(nums)):
#         prefix[i] = prefix[i - 1] + nums[i]

#     return prefix


# with new array
def running_sum(nums):
    prefix = [nums[0]]

    for i in range(1, len(nums)):
        prefix.append(prefix[-1] + nums[i])

    return prefix

    # Time Complexity: O(n), where n is the length of the input array nums.
    # This is because we iterate through the array once, performing constant time operations at each step.
    #
    # Space Complexity: O(n), as we create a new array prefix to store the running sum.
    # The size of prefix is the same as the input array nums.


# in place
def running_sum2(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]
    return nums

    # Time Complexity: O(n), where n is the length of the input array nums.
    # This is because we iterate through the array once, performing constant time operations at each step.
    #
    # Space Complexity: O(1), as we modify the input array in-place without using any additional space.


nums = [3, 1, 2, 10, 1]

print(running_sum(nums))
print(running_sum2(nums))
# Output: [3, 4, 6, 16, 17]
