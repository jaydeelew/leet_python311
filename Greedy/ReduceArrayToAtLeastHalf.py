# You are given an integer array arr. You can choose a set of integers and remove all the occurrences
# of these integers in the array.
# Return the minimum size of the set so that at least half of the integers of the array are removed.
from collections import Counter


class Solution:
    def minSetSize(self, arr: list[int]) -> int:
        counts = Counter(arr)
        counts = sorted(counts.values(), reverse=True)
        half_len = len(arr) / 2
        ans = 0

        for c in counts:
            half_len -= c
            ans += 1
            if half_len <= 0:
                return ans
        return ans


# arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
# # Output: 2

arr = [7, 7, 7, 7, 7, 7]
# Output: 1

sol = Solution()
print(sol.minSetSize(arr))
