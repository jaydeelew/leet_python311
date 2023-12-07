# 695. You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.


class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        def isValid(row, col):
            return 0 <= row < row_len and 0 <= col < col_len and grid[row][col] == 1

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()

        def dfs(row, col):
            area = 0
            for dx, dy in directions:
                row_adjacent, col_adjacent = row + dx, col + dy
                if isValid(row_adjacent, col_adjacent) and (row_adjacent, col_adjacent) not in seen:
                    seen.add((row_adjacent, col_adjacent))
                    # area is cumulative with every dfs() call below it on the stack
                    # add one for this current valid neighbor who has not been seen
                    area += dfs(row_adjacent, col_adjacent) + 1
            return area

        max_area = 0
        for x in range(row_len):
            for y in range(col_len):
                if grid[x][y] == 1 and (x, y) not in seen:
                    seen.add((x, y))
                    # Add 1 to result of dfs to include coordinate dfs was called with
                    max_area = max(max_area, 1 + dfs(x, y))
        return max_area

    def maxAreaOfIsland_Iterative(self, grid: list[list[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        def isValid(row, col):
            return 0 <= row < row_len and 0 <= col < col_len and grid[row][col] == 1

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        seen = set()
        stack = []

        def dfs(row, col):
            # must push initial unseen node onto stack
            stack.append((row, col))
            area = 0
            while stack:
                coordinate = stack.pop()
                for dx, dy in directions:
                    row_adjacent, col_adjacent = coordinate[0] + dx, coordinate[1] + dy
                    if isValid(row_adjacent, col_adjacent) and (row_adjacent, col_adjacent) not in seen:
                        seen.add((row_adjacent, col_adjacent))
                        # push valid neighbor onto stack
                        stack.append((row_adjacent, col_adjacent))
                        area += 1
            return area

        max_area = 0
        for x in range(row_len):
            for y in range(col_len):
                if grid[x][y] == 1 and (x, y) not in seen:
                    seen.add((x, y))
                    # Add 1 to result of dfs to include coordinate dfs was called with
                    max_area = max(max_area, 1 + dfs(x, y))
        return max_area


grid = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
# Output: 6

sol = Solution()
print(sol.maxAreaOfIsland(grid))
