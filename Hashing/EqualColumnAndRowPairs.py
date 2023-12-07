# 2352. Equal Row and Column Pairs
# Given an n x n matrix grid, return the number of pairs (R, C) where R is a row and C is a column,
# and R and C are equal if we consider them as 1D arrays.

from collections import defaultdict


class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        grid_rows = defaultdict(int)
        for row in grid:
            # need to convert row from list to tuple since dic keys are immutable types
            grid_rows[tuple(row)] += 1

        grid_columns = defaultdict(int)
        for i in range(len(grid[0])):
            column_build = []
            for row in grid:
                column_build.append(row[i])
            grid_columns[tuple(column_build)] += 1

        num_of_pairs = 0
        for row in grid_rows:
            # if row does not in grid_columns, defaultdict returns 0
            num_of_pairs += grid_rows[row] * grid_columns[row]

        return num_of_pairs


# grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]  # returns 1
# grid = [[5, 4, 2], [4, 0, 1], [2, 1, 5]]  # returns 3
grid = [[1, 1, 0], [1, 1, 0], [0, 5, 5]]  # returns 2

sol = Solution()
print(sol.equalPairs(grid))
