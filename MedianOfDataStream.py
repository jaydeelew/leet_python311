# 295. Find Median from Data Stream
# The median is the middle value in an ordered integer list.
# If the size of the list is even, the median is the average of the two middle values.
# Implement the MedianFinder class:
# MedianFinder() initializes the MedianFinder object.
# void addNum(int num) adds the integer num to the data structure.
# double findMedian() returns the median of all elements so far.


import heapq


class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        # push num to max heap (num is heapified by the method)
        # pop max heap and push to min heap
        # previous two steps will lead to min heap being greater than max heap
        # when min heap > max heap, pop from min heap and push to max heap
        # result is either size of min heap & max heap will be equal, or max heap will be greater by one
        heapq.heappush(self.max_heap, -num)  # negate num to maintain max heap, push to correct postion
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))  # negate popped top of max heap (to make + for min heap)
        # if size of min heap is greater by one, make max heap greater by one
        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # if max heap is greater by one, negating the top of heap will be the median
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # else the median is the addition (recall max heap values are negative) of the top of both heaps divided by two
        return (self.min_heap[0] - self.max_heap[0]) / 2


medianFinder = MedianFinder()
medianFinder.addNum(1)  # arr = [1]
medianFinder.addNum(2)  # arr = [1, 2]
print(medianFinder.findMedian())  # return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3)  # arr[1, 2, 3]
print(medianFinder.findMedian())  # return 2.0
