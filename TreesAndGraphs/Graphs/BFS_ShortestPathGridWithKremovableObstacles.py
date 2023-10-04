# 1293. Shortest Path in a Grid with Obstacles Elimination
# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle).
# You can move up, down, left, or right from and to an empty cell in one step.
# Return the minimum number of steps to walk from the upper left corner to the lower right corner given that
# you can eliminate at most k obstacles. If it is not possible, return -1.

from collections import deque


class Solution:
    def shortestPath(self, grid: list[list[int]], k: int) -> int:
        def valid(row, col):
            # cell position and not value considered in this case since cell value (0 or 1) may be overcome by 'remain'
            return 0 <= row < m and 0 <= col < n

        m = len(grid)  # rows
        n = len(grid[0])  # columns
        queue = deque([(0, 0, k, 0)])  # row, col, obstacles remaining, steps
        seen = {(0, 0, k)}  # make a distinction between same cell with different remaining qty (each entry is a state)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, remain, steps = queue.popleft()
            if row == m - 1 and col == n - 1:
                return steps

            for dx, dy in directions:
                adj_row, adj_col = row + dy, col + dx
                if valid(adj_row, adj_col):
                    if grid[adj_row][adj_col] == 0:
                        if (adj_row, adj_col, remain) not in seen:
                            seen.add((adj_row, adj_col, remain))
                            queue.append((adj_row, adj_col, remain, steps + 1))
                    # otherwise, it is an obstacle and we can only pass if we have remaining removals
                    elif remain and (adj_row, adj_col, remain - 1) not in seen:
                        seen.add((adj_row, adj_col, remain - 1))
                        # each entry(state) in queue contains how many steps it took to arrive to it
                        queue.append((adj_row, adj_col, remain - 1, steps + 1))

        return -1


sol = Solution()

k = 1
grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]  # ouptut: 6

# k = 1
# grid = [[0, 1, 1], [1, 1, 1], [1, 0, 0]]  # output: -1

print(sol.shortestPath(grid, k))
