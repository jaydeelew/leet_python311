# Example 3: 2342. Max Sum of a Pair With Equal Sum of Digits
# Given an array of integers nums, find the maximum value of nums[i] + nums[j],
# where nums[i] and nums[j] have the same digit sum (the sum of their individual digits).
# Return -1 if there is no pair of numbers with the same digit sum.

from collections import defaultdict


class Solution:
    def sumDigits(self, num: int) -> int:
        return 0 if num == 0 else int(num % 10) + self.sumDigits(int(num / 10))
        #  recursive function example sumDigits(321):
        #  f(321): return 1 + f(32) = 6
        #  f(32): return 2 + f(3) = 5
        #  f(3): return 3 + f(0) = 3
        #  f(0): return 0 (base case)


    def maximumSum(self, nums: list[int]) -> int:
        equal_sums = defaultdict(list)
        for num in nums:
            num_sum = self.sumDigits(num)  # sum the digits in num
            equal_sums[num_sum].append(num)  # the sum of digits in a num will be key, each num will be added to key's value list

        max_pair = float("-inf")
        for key in equal_sums:
            if len(equal_sums[key]) >= 2:  # make sure there exits at least a pair of numbers with equal digit-sum
                equal_sums[key].sort(reverse=True)  # reverse sort the list at equal_sums[key] in-place
                max_pair = max(max_pair, equal_sums[key][0] + equal_sums[key][1])  # the first two elements in list are largest

        return max_pair if max_pair != float("-inf") else -1


nums = [321, 123, 51, 654, 4533, 999]
sol = Solution()
print(sol.maximumSum(nums))