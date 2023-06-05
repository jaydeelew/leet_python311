# turn mutable list into immutable tuple

from typing import List


class Solution:
    def listToTuple(self, arr: List[int]) -> tuple:
        result = tuple(arr)
        return result


list = [5, 6, 1, 8, 0, 2]
sol = Solution()
print(sol.listToTuple(list))
