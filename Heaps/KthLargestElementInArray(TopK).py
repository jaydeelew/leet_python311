# 215. Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?
import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]


nums = [3, 2, 1, 5, 6, 4]
k = 2
# # Output: 5

# nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
# k = 4
# Output: 4

sol = Solution()
print(sol.findKthLargest(nums, k))
