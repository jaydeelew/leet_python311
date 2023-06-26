# Example 3: 2342. Max Sum of a Pair With Equal Sum of Digits
# Given an array of integers nums, find the maximum value of nums[i] + nums[j],
# where nums[i] and nums[j] have the same digit sum (the sum of their individual digits).
# Return -1 if there is no pair of numbers with the same digit sum.

from collections import defaultdict


class Solution:
    def sum_digits(self, num: int) -> int:
        return 0 if num == 0 else int(num % 10) + self.sum_digits(int(num / 10))
        #  recursive function example sumDigits(321):
        #  f(321): return 1 + f(32) = 6
        #  f(32): return 2 + f(3) = 5
        #  f(3): return 3 + f(0) = 3
        #  f(0): return 0 (base case)

    def maximum_sum(self, nums: list[int]) -> int:
        # equal_sums = defaultdict(list)
        # for num in nums:
        #     num_sum = self.sum_digits(num)  # sum the digits in num
        #     equal_sums[num_sum].append(num)  # the sum of digits in a num is the key, each num will be added to key's value list
        #
        # max_pair = -1
        # for key in equal_sums:
        #     curr = equal_sums[key]
        #     if len(curr) >= 2:  # make sure there exits at least a pair of numbers with equal digit-sum
        #         curr.sort(reverse=True)  # reverse sort the list at equal_sums[key] in-place
        #         max_pair = max(max_pair, curr[0] + curr[1])  # the first two elements in list are largest

        max_val_of_same_digit_sums = defaultdict(int)  # key is digit-sum of a num, val is max num value of equal sum nums so far
        max_pair = -1
        for num in nums:
            digit_sum = self.sum_digits(num)
            if digit_sum in max_val_of_same_digit_sums:  # if current num digit-sum is an existing key
                # max_pair is greatest max value of equal digit-sums plus current num
                max_pair = max(max_pair, max_val_of_same_digit_sums[digit_sum] + num)
            # if current num is greater than largest num seen thus far, assign current num
            max_val_of_same_digit_sums[digit_sum] = max(max_val_of_same_digit_sums[digit_sum], num)

        return max_pair


nums = [321, 123, 51, 654, 4533, 999]
sol = Solution()
print(sol.maximum_sum(nums))
