# 973. Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
# return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
import math
import heapq


class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        heap = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(heap, (-distance, [x, y]))
            if len(heap) > k:
                heapq.heappop(heap)
        return [pair[1] for pair in heap]


# points = [[1, 3], [-2, 2]]
# k = 1
# # Output: [[-2,2]]

points = [[3, 3], [5, -1], [-2, 4]]
k = 2
# Output: [[3,3],[-2,4]]

sol = Solution()
print(sol.kClosest(points, k))
