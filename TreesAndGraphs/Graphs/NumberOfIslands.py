# 200. Number of Islands
# Given an m x n 2D binary grid which represents a map of 1 (land) and 0 (water),
# return the number of islands. An island is surrounded by water and is formed by connecting adjacent
# land cells horizontally or vertically.


class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])

        def valid(row, col):
            # return True if row and column lengths are within bounds and grid location is 1
            return 0 <= row < row_len and 0 <= col < col_len and grid[row][col] == "1"

        seen = set()  # set of (row, col) tuples
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(row, col):
            for dx, dy in directions:
                adjacent_row, adjacent_col = row + dy, col + dx
                # if adjacent (row, col) is valid and (row, col) is not in seen...
                if valid(adjacent_row, adjacent_col) and (adjacent_row, adjacent_col) not in seen:
                    seen.add((adjacent_row, adjacent_col))
                    dfs(adjacent_row, adjacent_col)

        ans = 0
        for row in range(row_len):
            for col in range(col_len):
                if grid[row][col] == "1" and (row, col) not in seen:
                    ans += 1
                    seen.add((row, col))
                    dfs(row, col)

        return ans


grid_return_1 = [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]
grid_return_2 = [["1", "0", "0", "0", "1"], ["1", "0", "0", "0", "1"], ["1", "0", "0", "0", "1"], ["1", "0", "0", "0", "1"]]
grid_return_3 = [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]
sol = Solution()
print(sol.numIslands(grid_return_3))
