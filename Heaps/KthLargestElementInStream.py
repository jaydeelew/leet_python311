# Design a class to find the kth largest element in a stream.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Implement KthLargest class:
# KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
# int add(int val) Appends the integer val to the stream and returns the element representing
# the kth largest element in the stream.
import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)  # min heap

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        # reduce min heap to largest k values
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]  # return smallest value which is kth largest


# kthlargest = KthLargest(3, [4, 5, 8, 2])
# print(kthlargest.add(3))  # return 4
# print(kthlargest.add(5))  # return 5
# print(kthlargest.add(10))  # return 5
# print(kthlargest.add(9))  # return 8
# print(kthlargest.add(4))  # return 8

kthlargest = KthLargest(1, [])
print(kthlargest.add(-3))  # return -3
print(kthlargest.add(-2))  # return -2
print(kthlargest.add(-4))  # return -2
print(kthlargest.add(0))  # return 0
print(kthlargest.add(4))  # return 4
