# Example 2: 239. Sliding Window Maximum

# Given an integer array nums and an integer k, there is a sliding window of size k that moves
# from the very left to the very right. For each window, find the maximum element in the window.

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        queue = deque()
        for i in range(len(nums)):
            # maintain monotonic decreasing
            # all elements in the deque smaller than the current one
            # have no chance of being the maximum, so get rid of them
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()

            queue.append(i)

            # queue[0] is the index of the maximum element.
            # if queue[0] + k == i, then it is outside the window
            if queue[0] + k == i:
                queue.popleft()

            # only add to the answer once our window has reached size k
            if i >= k - 1:
                ans.append(nums[queue[0]])

        return ans


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
# return [3, 3, 5, 5, 6, 7]
sol = Solution()
print(sol.maxSlidingWindow(nums, k))
