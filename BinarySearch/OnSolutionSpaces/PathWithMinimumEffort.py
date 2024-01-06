# 1631. Path With Minimum Effort
# You are given heights, a positive 2D array of size m x n, where heights[row][col] represents the height of cell (row, col).
# You can move up, down, left, or right. A path's effort is the largest absolute difference you can have between
# any two consecutive cells traversed. Return the minimum effort required to get from the top left to the bottom right.


class Solution:
    def minimumEffortPath(self, heights: list[list[int]]) -> int:
        def valid(row, col):
            return 0 <= row < row_len and 0 <= col < col_len

        def check(effort):
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            seen = {(0, 0)}  # set of tuples
            stack = [(0, 0)]  # list of tuples

            while stack:
                row, col = stack.pop()
                if (row, col) == (row_len - 1, col_len - 1):
                    return True

                for dx, dy in directions:
                    # note change in y is change in row, change in x is change in column
                    next_row, next_col = row + dy, col + dx
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))

            return False

        row_len = len(heights)
        col_len = len(heights[0])
        left = 0
        # find the largest number in heights by first iterating over each row and finding
        # max of each row while maintaining the max of the max of each row
        right = max(max(row) for row in heights)
        while left <= right:
            mid = (left + right) // 2
            # if check returns True, value of mid was able to reach bottom right of matrix
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left


heights = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
# Output: 2

# heights = [[1,2,3],[3,8,4],[5,3,5]]
# # Output: 1

# heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
# # Output: 0

sol = Solution()
print(sol.minimumEffortPath(heights))
