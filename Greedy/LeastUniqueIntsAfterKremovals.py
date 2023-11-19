# Example 4: 1481. Least Number of Unique Integers after K Removals
# Given an array of integers arr and an integer k,
# find the least number of unique integers after removing exactly k elements.
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        counts = Counter(arr)
        # sorted_counts = sorted(counts.items(), key=lambda x: x[1])
        sorted_counts = sorted(counts.values())
        ans = len(counts)
        i = 0

        while k:

        return ans


arr = [5, 5, 4]
k = 1 w
# Output: 1

# arr = [4, 3, 1, 1, 3, 3, 2]
# k = 3
# # Output: 2

# arr = [1]
# k = 1

sol = Solution()
print(sol.findLeastNumOfUniqueInts(arr, k))
