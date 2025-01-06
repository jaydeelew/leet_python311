# 52. N-Queens II
# The N-Queens puzzle is the famous problem of placing n queens on an n x n chessboard such that
# no two queens attack each other. Given an integer n, return the number of distinct solutions to the N-Queens puzzle.
# For those who don't play chess: a queen can attack along the row, column, and diagonals it occupies.


class Solution:
    def totalNQueens(self, n):
        def backtrack(row, diagonals, anti_diagonals, cols):
            # base case arrived at when n queens have been placed
            # and when no column or diagonal has more than one queen
            if row == n:
                return 1  # will add to solution

            solutions = 0

            for col in range(n):
                # rows - cols creates diagonals from top left to bottom right of the same difference
                curr_diagonal = row - col
                # rows + cols creates diagonals from top right to bottom left of the same sum
                curr_anti_diagonal = row + col
                # If the queen is not placeable
                if col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals:
                    continue

                # "Add" the queen to the board
                # rows are not dealt with here since we only need to be able to
                # add a queen, not sharing any columns or diagonals with another, n times (the number of rows)
                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)

                # Move on to the next row with the updated board state
                solutions += backtrack(row + 1, diagonals, anti_diagonals, cols)

                # "Remove" the queen from the board since we have already
                # explored all valid paths using the above function call
                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)

            return solutions

        return backtrack(0, set(), set(), set())


n = 4
# Output: 2

# n = 1
# Output: 1

sol = Solution()
print(sol.totalNQueens(n))
