# Given an array of integers nums, you start with an initial positive value startValue.
# In each iteration, you calculate the step by step sum of startValue plus elements in nums (from left to right).
# Return the minimum positive value of startValue such that the step by step sum is never less than 1.


def minStartValue(nums):
    currentmin = runningsum = 0
    for i in nums:
        runningsum += i
        currentmin = min(currentmin, runningsum)

    return 1 - currentmin  # min value is zero, so return value will always be greater than 0


nums = [-3, 2, -3, 4, 2]
print(minStartValue(nums))
