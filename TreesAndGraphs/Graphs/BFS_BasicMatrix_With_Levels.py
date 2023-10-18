from collections import deque


class Solution:
    def findCoordinates(self, matrix: list[list[int]], target: int) -> tuple:
        num_of_rows = len(matrix)
        num_of_cols = len(matrix[0])

        def valid(row, col):
            return 0 <= row < num_of_rows and 0 <= col < num_of_cols

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # adjacent cells
        queue = deque([(0, 0)])
        seen = {(0, 0)}  # if its been in the queue(see above), it's been seen
        steps = 0
        while queue:
            # do level work starting here
            num_coords_in_queue = len(queue)
            for _ in range(num_coords_in_queue):
                row, col = queue.popleft()
                # do coordinate work starting here
                if matrix[row][col] == target:
                    return (row, col, steps)
                for dx, dy in directions:
                    adj_row, adj_col = row + dy, col + dx
                    if valid(adj_row, adj_col) and (adj_row, adj_col) not in seen:
                        seen.add((adj_row, adj_col))
                        queue.append((adj_row, adj_col))
            steps += 1
        return (-1, -1, -1)  # (row, col, steps)


sol = Solution()
target = 3
matrix = [
    [1, 15, 0, 16, 5],
    [13, 19, 4, 12, 2],
    [8, 17, 11, 6, 9],
    [14, 7, 10, 18, 3],
]
print(sol.findCoordinates(matrix, target))
