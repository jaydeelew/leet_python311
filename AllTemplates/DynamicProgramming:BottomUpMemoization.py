# def fn(arr):
#     dp = [0] * len(arr)
#     dp[BASE_CASE] = VALUE

#     for i in arr:
#         dp[i] = RECURRENCE_RELATION

#     return dp[i]


# Given an integer array nums, return the length of the longest strictly increasing subsequence.


def lengthOfLIS_iter(nums: list[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
