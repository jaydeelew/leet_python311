# Given an array of non-negative integers arr, you are initially positioned at start index of the array.
# When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach any index with value 0.
# Notice that you can not jump outside of the array at any time.
from collections import deque


class Solution:
    def canReach(self, arr: list[int], start: int) -> bool:
        queue = deque([start])  # queue of arr indexes
        seen = {start}
        while queue:
            arr_index = queue.pop()
            jump = arr[arr_index]
            if jump == 0:
                return True
            for j in [-jump, jump]:
                next_index = arr_index + j
                if 0 <= next_index < len(arr):
                    if next_index not in seen:
                        queue.append(next_index)
                        seen.add(next_index)
        return False


sol = Solution()

arr = [4, 2, 3, 0, 3, 1, 2]
start = 5
# Output: true

# arr = [4,2,3,0,3,1,2]
# start = 0
# # Output: true

# arr = [3, 0, 2, 1, 2]
# start = 2
# # Output: false

print(sol.canReach(arr, start))
