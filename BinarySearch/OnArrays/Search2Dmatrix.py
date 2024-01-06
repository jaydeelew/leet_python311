# 74. Search a 2D Matrix
# Write an efficient algorithm that searches for a value target in an m x n integer matrix.
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.


class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        r_len = len(matrix)
        c_len = len(matrix[0])
        left = 0
        right = (r_len * c_len) - 1

        while left <= right:
            mid = (left + right) // 2
            row = mid // c_len
            col = mid % c_len
            mid_val = matrix[row][col]
            if mid_val == target:
                return True
            if target < mid_val:
                right = mid - 1
            else:
                left = mid + 1

        return False


sol = Solution()

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 3
# Output: true

# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# target = 13
# # Output: false

print(sol.searchMatrix(matrix, target))
