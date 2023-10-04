# 542. 01 Matrix
# Given an m x n binary (every element is 0 or 1) matrix mat, find the distance of the nearest 0 for each cell.
# The distance between adjacent cells (horizontally or vertically) is 1.
# If the cell is 0, then the distance to the nearest 0 is 0

from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        def valid(row, col):
            return 0 <= row < num_of_rows and 0 <= col < num_of_cols and mat[row][col] == 1

        # a copy of matrix can be made here, modified, and returned instead of the original
        num_of_rows = len(mat)
        num_of_cols = len(mat[0])
        queue = deque()
        seen = set()

        # for cells that are 0, build initial bfs level of cells on queue with a steps value of 1 for each entry
        # so that cells adjacent to 0 cells will be updated to 1
        for row in range(num_of_rows):
            for col in range(num_of_cols):
                if mat[row][col] == 0:
                    queue.append((row, col, 1))  # row, col, steps
                    seen.add((row, col))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # adjacent cells

        while queue:
            row, col, steps = queue.popleft()

            for dx, dy in directions:
                adjacent_row, adjacent_col = row + dy, col + dx  # change in row is on y-axis, change in col is on x-axis
                if valid(adjacent_row, adjacent_col) and (adjacent_row, adjacent_col) not in seen:
                    seen.add((adjacent_row, adjacent_col))
                    # increment steps to that the next bfs level of adjacent cells will reflect distance from nearest 0
                    queue.append((adjacent_row, adjacent_col, steps + 1))
                    mat[adjacent_row][adjacent_col] = steps

        return mat


sol = Solution()
mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]  # Output: [[0,0,0],[0,1,0],[1,2,1]]
# mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]  # Output: [[0,0,0],[0,1,0],[0,0,0]]
print(sol.updateMatrix(mat))
