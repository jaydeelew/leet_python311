# 300. Longest Increasing Subsequence (recursive)
# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# The term strictly means that there are not any duplicates in the subsequence.
# Solve using a top-down/recursive memoization method


def lsisRecursive(nums: list[int]) -> int:
    memo = {}

    def dp(i):
        # Check if the result for this state is already computed
        if i in memo:
            return memo[i]

        # 1 for the subsequence containing only nums[i] (nums[i] being not greater than any previous nums[j])
        ans = 1
        for j in range(i):
            if nums[j] < nums[i]:
                # we maintain the max subsequence up to and including i,
                # i is included by adding 1 with dp(j) + 1 below
                ans = max(ans, dp(j) + 1)
        # memo[i] is assigned 1 if there was no previous num[j] less than num[i],
        # since the only subsequence is the current element.
        memo[i] = ans
        return ans

    # Compute the length of the longest increasing subsequence for each element
    # and return the maximum length using a generator expression
    return max(dp(i) for i in range(len(nums)))


nums = [5, 2, 4, 3, 6]
# Output: 3

# nums = [10, 9, 2, 5, 3, 7, 101, 18]
# Output: 4

# nums = [0, 1, 0, 3, 2, 3]
# Output: 4

# nums = [7, 8, 1, 2, 3]
# Output: 3

# nums = [7, 7, 7, 7, 7, 7, 7]
# Output: 1

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Output: 10

print(lsisRecursive(nums))
