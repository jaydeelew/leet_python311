# 2389. Longest Subsequence With Limited Sum
# You are given an integer array nums of length n, and an integer array queries of length m.
# Return an array answer of length m where answer[i] is the maximum size of a subsequence that
# you can take from nums such that the sum of its elements is less than or equal to queries[i].
# A subsequence is an array that can be derived from another array by deleting some or no elements
# without changing the order of the remaining elements.


class Solution:
    def answerQueries(self, nums: list[int], queries: list[int]) -> list[int]:
        nums.sort()
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])

        ans = []
        for val in queries:
            left = 0
            right = len(nums) - 1
            done_while_loop = False
            while left <= right:
                mid = (left + right) // 2
                if val == prefix_sum[mid]:
                    ans.append(mid + 1)
                    done_while_loop = True
                    break
                elif val < prefix_sum[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            if done_while_loop:
                continue
            ans.append(left)

        return ans


# nums = [4, 5, 2, 1]
# queries = [3, 10, 21]
# # Output: [2,3,4]

nums = [2, 3, 4, 5]
queries = [1]
# Output: [0]

sol = Solution()
print(sol.answerQueries(nums, queries))
