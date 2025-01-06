# 410. Given an integer array nums and an integer k, split nums into k non-empty subarrays
# such that the largest sum of any subarray is minimized.
# Return the minimized largest sum of the split.
# A subarray is a contiguous part of the array.


class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def check_if_can_split_into_k_subarrays(val):
            curr_sum = 0
            num_of_splits = 0
            for num in nums:
                if curr_sum + num <= val:
                    curr_sum += num
                else:
                    curr_sum = num
                    num_of_splits += 1

            # number of splits plus one is the number of subarrays
            # return True for a number of subarrays less than k,
            # otherwise values less than mid would never be evaluated
            return True if num_of_splits + 1 <= k else False

        # the minimum value for the largest subarray sum
        left = max(nums)
        # the maximum value for the largest subarray sum
        right = sum(nums)
        # the minimizing form of binary search
        minmized_largest_subarray_sum = 0
        while left <= right:
            mid = left + (right - left) // 2
            if check_if_can_split_into_k_subarrays(mid):
                right = mid - 1
                # the latest mid that can be split into a valid number of subarrays
                # will be the minimum largest subarray of the split
                minmized_largest_subarray_sum = mid
            else:
                left = mid + 1

        return minmized_largest_subarray_sum


# nums = [7, 2, 5, 10, 8]
# k = 2
# # Output: 18

# nums = [1, 2, 3, 4, 5]
# k = 2
# # Output: 9

nums = [1, 4, 4]
k = 3
# Output: 4

sol = Solution()
print(sol.splitArray(nums, k))
