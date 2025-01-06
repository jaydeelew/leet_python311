# 79. Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.


class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        # if row and column are within the grids boundaries
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        # i is the index (letter) of the word we are checking existence for in the grid.
        def backtrack(row, col, i, seen):
            # if we reach the end of the word
            if i == len(word):
                return True

            # for change in x and change in y
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                # check if within bounds and make sure not to visit same point on the grid again.
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    if board[next_row][next_col] == word[i]:
                        # use seen to avoid using the same letter in the same path
                        seen.add((next_row, next_col))
                        # increase i to move to the next letter
                        if backtrack(next_row, next_col, i + 1, seen):
                            return True
                        # if not true backup one letter and start again
                        seen.remove((next_row, next_col))

            return False

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m = len(board)
        n = len(board[0])

        # check every point on the grid for the first letter of the word,
        # and if found, use backtrack to see if the entire word can be found.
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True

        return False


board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
word = "ABCCED"
# Output: true

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

sol = Solution()
print(sol.exist(board, word))
