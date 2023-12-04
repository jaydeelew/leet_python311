# Example 2: 2294. Partition Array Such That Maximum Difference Is K
# Given an integer array nums and an integer k, split nums into subsequences,
# where each subsequences' maximum and minimum element is within k of each other.
# What is the minimum number of subsequences needed?


class Solution:
    def partitionArray(self, nums: list[int], k: int) -> int:
        nums.sort()
        # if all values in nums are within a difference of k, then we return one sequence
        ans = 1
        # we begin by comparing the first value in nums to the next
        x = nums[0]

        # on the first iteration we compare nums[0] to nums[1]
        for i in range(1, len(nums)):
            # if the difference between the next sorted array element and x is greater than max difference k
            if nums[i] - x > k:
                # x begins a new subsequence
                x = nums[i]
                # add another subsequence
                ans += 1

        return ans


# nums = [3, 6, 1, 2, 5]
# k = 2
# # Output: 2

nums = [1, 2, 3]
k = 1
# Output: 2

sol = Solution()
print(sol.partitionArray(nums, k))
