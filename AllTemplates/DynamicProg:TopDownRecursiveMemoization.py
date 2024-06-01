# def fn(arr):
#     def dp(STATE):
#         if BASE_CASE:
#             return 0

#         if STATE in memo:
#             return memo[STATE]

#         ans = RECURRENCE_RELATION(STATE)
#         memo[STATE] = ans
#         return ans

#     memo = {}
#     return dp(STATE_FOR_WHOLE_INPUT)


# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# The term strictly means that there are not any duplicates in the subsequence.
# Provide the Top-Down Iterative Memoization solution.
def lengthOfLSIS_recursive(nums: list[int]) -> int:
    memo = {}

    def dp(i):
        # Check if the result for this state is already computed
        if i in memo:
            return memo[i]

        # 1 for the subsequence containing only nums[i] (nums[i] being not greater than any previous nums[j])
        ans = 1
        for j in range(i):
            if nums[j] < nums[i]:
                ans = max(ans, dp(j) + 1)

        memo[i] = ans
        return ans

    # Compute the length of the longest increasing subsequence for each element
    # and return the maximum length using a generator expression
    return max(dp(i) for i in range(len(nums)))


# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4

# nums = [0, 1, 0, 3, 2, 3]
# Output: 4

# nums = [7, 8, 1, 2, 3]
# Output: 3

# nums = [7, 7, 7, 7, 7, 7, 7]
# Output: 1

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: 10

print(lengthOfLSIS_recursive(nums))
