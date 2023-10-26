# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt.
# This area is in the shape of a circle with the center as the location of the bomb.
# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri].
# xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range.
# These bombs will further detonate the bombs that lie in their ranges.
# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.
from collections import deque, defaultdict
import math


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        if len(bombs) == 1:
            return 1

        graph = defaultdict(list)
        duplicates = defaultdict(list)
        max_exploded = 0

        for i in range(len(bombs)):
            bomb_tuple = tuple(bombs[i])
            graph[bomb_tuple]  # needed to add bombs to graph with no exploding neighbors
            for j in range(len(bombs)):
                if i != j and bombs[i] != bombs[j]:
                    diff_x = abs(bombs[j][0] - bombs[i][0])
                    diff_y = abs(bombs[j][1] - bombs[i][1])
                    distance = math.sqrt(diff_x**2 + diff_y**2)
                    if distance <= bombs[i][2]:  # if distance between bomb i and j is less than or equal bomb radius of i
                        graph[bomb_tuple].append(bombs[j])  # bomb j is a neighbor of bomb i
                elif i != j:  # the bombs are same position and radius, but are distinct bombs
                    if bomb_tuple not in duplicates:
                        duplicates[bomb_tuple].append([i, j, 1])  # one for the match, the original will be counted w/ q_sz below
                    elif i == duplicates[bomb_tuple][0][0]:  # only matches on this iteration of i to avoid repeat matches
                        duplicates[bomb_tuple][0][2] += 1  # one for each addtional match

        queue = deque()
        for x, y, r in graph.keys():
            queue.append((x, y, r))
            seen = {(x, y, r)}
            num_of_explosions = 0  # number of explosions this graph iteration
            while queue:
                q_sz = len(queue)
                num_of_explosions += q_sz
                for _ in range(q_sz):
                    x, y, r = queue.popleft()
                    if (x, y, r) in duplicates:
                        num_of_explosions += duplicates[(x, y, r)][0][2]
                    for nx, ny, nr in graph[(x, y, r)]:
                        if (nx, ny, nr) not in seen:
                            queue.append((nx, ny, nr))
                            seen.add((nx, ny, nr))
            max_exploded = max(max_exploded, num_of_explosions)

        return max_exploded


sol = Solution()

# bombs = [[2, 1, 3], [6, 1, 4]]
# # Output: 2

# bombs = [[1, 1, 5], [10, 10, 5]]
# # Output: 1

# bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]
# # Output: 5

# bombs = [[1, 1, 1]]
# # Output: 1

# bombs = [[4, 4, 3], [4, 4, 3], [4, 4, 3]]
# # Output: 3

bombs = [
    [6, 874, 154],
    [214, 633, 233],
    [786, 52, 144],
    [62, 561, 134],
    [643, 144, 17],
    [609, 578, 432],
    [553, 548, 433],
    [237, 992, 472],
    [16, 588, 323],
    [984, 826, 50],
    [210, 694, 143],
    [758, 74, 24],
    [363, 173, 116],
    [121, 741, 332],
    [274, 97, 147],
]
# Output: 11

# bombs = [
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
#     [10000, 10000, 1000],
# ]
# # Output: 100

print(sol.maximumDetonation(bombs))
