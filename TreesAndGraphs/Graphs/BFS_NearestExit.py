# 1926. You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.')
# and walls (represented as '+'). You are also given the entrance of the maze,
# where entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
# In one step, you can move one cell up, down, left, or right. You cannot step into a cell with a wall,
# and you cannot step outside the maze. Your goal is to find the nearest exit from the entrance.
# An exit is defined as an empty cell that is at the border of the maze. The entrance does not count as an exit.
# Return the number of steps in the shortest path from the entrance to the nearest exit,
# or -1 if no such path exists.
from collections import deque


class Solution:
    def nearestExit(self, maze: list[list[str]], entrance: list[int]) -> int:
        row_len = len(maze)
        col_len = len(maze[0])

        def valid(row: int, col: int) -> bool:
            return 0 <= row < row_len and 0 <= col < col_len and maze[row][col] != "+"

        def isBorder(row: int, col: int) -> bool:
            return row == 0 or row == row_len - 1 or col == 0 or col == col_len - 1

        x_start = entrance[0]
        y_start = entrance[1]
        queue = deque([(x_start, y_start, 0)])  # (row, col, steps)
        seen = {(x_start, y_start)}
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            row, col, steps = queue.popleft()
            if isBorder(row, col) and (row, col) != (x_start, y_start):
                return steps
            for dx, dy in directions:
                adjcnt_row, adjcnt_col = row + dy, col + dx
                if valid(adjcnt_row, adjcnt_col) and (adjcnt_row, adjcnt_col) not in seen:
                    queue.append((adjcnt_row, adjcnt_col, steps + 1))
                    seen.add((adjcnt_row, adjcnt_col))
        return -1


sol = Solution()

maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
# Output: 1

# maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
# entrance = [1, 0]
# # Output: 2

# maze = [[".", "+"]]
# entrance = [0, 0]
# # Output: -1

# maze = [["."]]
# entrance = [0, 0]
# # Output: -1

print(sol.nearestExit(maze, entrance))
