# 695. Max Area of Island
# You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
# connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.


def maxAreaOfIsland4(grid: list[list[int]]) -> int:
    if not grid:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    max_area = 0

    def dfs(i, j):
        if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] != 1:
            return 0

        grid[i][j] = "#"

        return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_area = max(max_area, dfs(i, j))

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

# grid = [[0, 0, 0, 0, 0, 0, 0, 0]]
# Output: 0

print(maxAreaOfIsland4(grid))
