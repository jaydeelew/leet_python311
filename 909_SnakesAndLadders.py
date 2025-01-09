# 909. Snakes and Ladders
# You are given an n x n integer matrix board where the cells are labeled from 1 to n^2 in a Boustrophedon style
# starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.
# You start on square 1 of the board. In each move, starting from square curr, do the following:
# Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n^2)].
# This choice simulates the result of a standard 6-sided die roll: i.e.,
# there are always at most 6 destinations, regardless of the size of the board.
# If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
# The game ends when you reach the square n^2.
# A board square on row r and column c has a snake or ladder if board[r][c] != -1.
# The destination of that snake or ladder is board[r][c]. Squares 1 and n^2 do not have a snake or ladder.
# Note that you only take a snake or ladder at most once per move.
# If the destination to a snake or ladder is the start of another snake or ladder,
# you do not follow the subsequent snake or ladder.
# For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2.
# You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
# Return the least number of moves required to reach the square n^2. If it is not possible to reach the square, return -1.
from collections import deque


class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)

        def label_to_position(label):
            # divmod explanation:
            # label-1 / width of row(i.e. n) = row to subtract from n
            # label-1 % width fo row(i.e. n) = index of col
            row, col = divmod(label - 1, n)  # label minus one to bring to zero indexing
            if row % 2 == 0:  # if even indexed row
                return n - 1 - row, col  # n-1 minus flips row counting to botton up
            else:  # if odd indexed row (labels in reverse order)
                return n - 1 - row, n - 1 - col  # n-1-column flips column counting to last-to-first

        seen = set()
        queue = deque()
        # initial label 1 is lower left corner of board, steps is zero
        queue.append((1, 0))
        while queue:
            label, step = queue.popleft()
            row, col = label_to_position(label)
            if board[row][col] != -1:
                # if label snake or ladder, change label to label at end of snake or ladder
                label = board[row][col]
            if label == n * n:
                return step
            for x in range(1, 7):
                new_label = label + x
                if new_label <= n * n and new_label not in seen:
                    seen.add(new_label)
                    queue.append((new_label, step + 1))
        return -1


sol = Solution()

# board = [
#     [-1, -1, -1, -1, -1, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 35, -1, -1, 13, -1],
#     [-1, -1, -1, -1, -1, -1],
#     [-1, 15, -1, -1, -1, -1],
# ]
# # Output: 4

board = [
    [-1, -1, -1, 135, -1, -1, -1, -1, -1, 185, -1, -1, -1, -1, 105, -1],
    [-1, -1, 92, -1, -1, -1, -1, -1, -1, 201, -1, 118, -1, -1, 183, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, 179, -1, -1, -1, -1, -1, -1],
    [-1, 248, -1, -1, -1, -1, -1, -1, -1, 119, -1, -1, -1, -1, -1, 192],
    [-1, -1, 104, -1, -1, -1, -1, -1, -1, -1, 165, -1, -1, 206, 104, -1],
    [145, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 229, -1],
    [-1, -1, 75, 140, -1, -1, -1, -1, -1, -1, -1, -1, 43, -1, 34, -1],
    [-1, -1, -1, -1, -1, -1, 169, -1, -1, -1, -1, -1, -1, 188, -1, -1],
    [-1, -1, -1, -1, -1, -1, 92, -1, 171, -1, -1, -1, -1, -1, -1, 66],
    [-1, -1, -1, 126, -1, -1, 68, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, 109, -1, 86, 28, 228, -1, -1, 144, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, 59, -1, -1, -1, -1, -1, 51, -1, -1, -1, 62, -1],
    [-1, 71, -1, -1, -1, 63, -1, -1, -1, -1, -1, -1, 212, -1, -1, -1],
    [-1, -1, -1, -1, 174, -1, 59, -1, -1, -1, -1, -1, -1, 133, -1, -1],
    [-1, -1, 62, -1, 5, -1, 16, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, 59, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
]
# Output: 10


# board = [
#     [-1, -1, -1, -1],
#     [-1, -1, -1, -1],
#     [-1, -1, -1, -1],
#     [-1, 15, -1, -1],
# ]
# # Output: 2

# board = [
#     [-1, 4, -1],
#     [6, 2, 6],
#     [-1, 3, -1],
# ]
# # Output: 2

# board = [
#     [-1, -1, 2, 21, -1],
#     [16, -1, 24, -1, 4],
#     [2, 3, -1, -1, -1],
#     [-1, 11, 23, 18, -1],
#     [-1, -1, -1, 23, -1],
# ]
# # Output: 2

# board = [
#     [-1, 10, -1, 15, -1],
#     [-1, -1, 18, 2, 20],
#     [-1, -1, 12, -1, -1],
#     [2, 4, 11, 18, 8],
#     [-1, -1, -1, -1, -1],
# ]
# # Output: 3

# board = [
#     [-1, 1, 2, -1],
#     [2, 13, 15, -1],
#     [-1, 10, -1, -1],
#     [-1, 6, 2, 8],
# ]
# # Output: 2

# board = [
#     [-1, -1, -1, -1, 48, 5, -1],
#     [12, 29, 13, 9, -1, 2, 32],
#     [-1, -1, 21, 7, -1, 12, 49],
#     [42, 37, 21, 40, -1, 22, 12],
#     [42, -1, 2, -1, -1, -1, 6],
#     [39, -1, 35, -1, -1, 39, -1],
#     [-1, 36, -1, -1, -1, -1, 5],
# ]
# # Output: 3

# board = [
#     [1, 1, -1],
#     [1, 1, 1],
#     [-1, 1, 1],
# ]
# # Output: -1

print(sol.snakesAndLadders(board))
