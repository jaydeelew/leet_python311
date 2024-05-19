# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# The term strictly means that there are not any duplicates in the subsequence.
# Provide the Bottom-Up Recursive Tabulation solution.

# def fn(arr):
#     dp = [0] * len(arr)
#     dp[BASE_CASE] = VALUE

#     for i in arr:
#         dp[i] = RECURRENCE_RELATION

#     return dp[i]


# as we iterate through the array, we keep track of the longest strictly increasing subsequence
# at each index, and at the end, we return the longest (max) strictly increasing subsequence
def lengthOfLSIS_iterative(nums: list[int]) -> int:
    # this is where we store the longest strictly increasing subsequence at each index
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            # if nums[j] < nums[i], then nums[i] is part of the longest strictly increasing subsequence
            if nums[j] < nums[i]:
                # so we update the dp value for the current index to the max of the current value
                # and the value at the previous index + 1 (plus 1 because we found a new number to add to the length).
                # dp[i] can be increasing or decreasind as the for j loop iterates to just before i,
                # this is why we need to get the max
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4

nums = [0, 1, 0, 3, 2, 3]
# Output: 4

# nums = [7, 8, 1, 2, 3]
# Output: 3

# nums = [7, 7, 7, 7, 7, 7, 7]
# Output: 1

print(lengthOfLSIS_iterative(nums))
