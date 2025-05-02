# 1380. Lucky Numbers in a Matrix
# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is
# the minimum element in its row and maximum in its column.


def luckyNumbers(matrix: list[list[int]]) -> list[int]:
    min_row = {min(row) for row in matrix}
    # *matrix unpacks into [3, 7, 8], [9, 11, 13], [15, 16, 17]
    # zip creates tuples: (3, 9, 15), (7, 11, 16), (8, 13, 17)
    max_col = {max(col) for col in zip(*matrix)}
    return list(min_row & max_col)


matrix = [
    [3, 7, 8],
    [9, 11, 13],
    [15, 16, 17],
]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

# matrix = [
#     [1, 10, 4, 2],
#     [9, 3, 8, 7],
#     [15, 16, 17, 12],
# ]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

# matrix = [[7, 8], [1, 2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

print(luckyNumbers(matrix))
