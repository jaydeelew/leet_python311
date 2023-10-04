# 1091. Shortest Path in Binary Matrix
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
# If there is no clear path, return -1. A clear path is a path from the top-left cell (0, 0)
# to the bottom-right cell (n - 1, n - 1) such that all visited cells are 0.
# You may move 8-directionally (up, down, left, right, or diagonally).


from collections import deque


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        def valid(row, col):
            return 0 <= row < n and 0 <= col < n and grid[row][col] == 0

        n = len(grid)
        seen = {(0, 0)}
        queue = deque([(0, 0, 0)])  # row, col, steps
        directions = [(0, 1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1), (0, -1), (-1, 0)]

        while queue:
            row, col, steps = queue.popleft()
            if (row, col) == (n - 1, n - 1):
                return steps

            for dx, dy in directions:
                adjacent_row, adjacent_col = row + dy, col + dx
                if valid(adjacent_row, adjacent_col) and (adjacent_row, adjacent_col) not in seen:
                    seen.add((adjacent_row, adjacent_col))
                    queue.append((adjacent_row, adjacent_col, steps + 1))  # each node in queue holds number of steps to get to it
        return -1


sol = Solution()

# grid = [[0, 1], [1, 0]]  # output: 1
# grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]  # output: -1
grid = [[0, 0, 1, 1, 1, 1], [0, 1, 0, 1, 1, 1], [0, 1, 1, 0, 1, 1], [0, 0, 0, 0, 0, 1], [1, 1, 1, 1, 0, 0], [1, 1, 1, 1, 1, 0]]
# output: 6

print(sol.shortestPathBinaryMatrix(grid))
