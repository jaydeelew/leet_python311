# 1481. Least Number of Unique Integers after K Removals
# Given an array of integers arr and an integer k,
# find the least number of unique integers after removing exactly k elements.
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: list[int], k: int) -> int:
        counts = Counter(arr)
        # sorted returns a list in ascending order
        sorted_counts = sorted(counts.values())
        ans = len(counts)

        for cnt in sorted_counts:
            if cnt <= k:
                ans -= 1
                k -= cnt
            else:
                return ans
        return ans


# arr = [5, 5, 4]
# k = 1
# # Output: 1

# arr = [4, 3, 1, 1, 3, 3, 2]
# k = 3
# # Output: 2

arr = [1]
k = 1
# Output: 0

sol = Solution()
print(sol.findLeastNumOfUniqueInts(arr, k))
