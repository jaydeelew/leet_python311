# 1129. Shortest Path with Alternating Colors
# You are given a directed graph with n nodes labeled from 0 to n - 1.
# Edges are red or blue in this graph. You are given redEdges and blueEdges,
# where redEdges[i] and blueEdges[i] both have the format [x, y] indicating an edge from x to y in the respective color.
# Return an array ans of length n, where answer[i] is the length of the shortest path
# from 0 to i where edge colors alternate, or -1 if no path exists.

from collections import defaultdict, deque


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        RED = 0
        BLUE = 1
        graph = [defaultdict(list), defaultdict(list)]
        for x, y in redEdges:
            # append: dictionary(color), key(from edge), value(to edge)
            graph[RED][x].append(y)
        for x, y in blueEdges:
            graph[BLUE][x].append(y)

        # Alternatively:
        # graph = defaultdict(lambda: defaultdict(list)) # dictionary of dictionaries of lists
        # for x, y in redEdges:
        #     graph[RED][x].append(y)
        # for x, y in blueEdges:
        #     graph[BLUE][x].append(y)

        ans = [float("inf")] * n
        # node, color, steps
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        # a state in seen is made up of node & color
        seen = {(0, RED), (0, BLUE)}

        while queue:
            # color is 0 or 1 (red or blue)
            node, color, steps = queue.popleft()
            # min of steps so far btwn answer list (starting at inf) and steps of current node
            ans[node] = min(ans[node], steps)

            # color is which dictionary, node is which key, neighbors are values of keys
            for neighbor in graph[color][node]:
                # if neignbor is the other color and not yet seen (same color is ignored)
                if (neighbor, 1 - color) not in seen:
                    # 1 - color flips color
                    seen.add((neighbor, 1 - color))
                    # steps are incremented for this node up encountering the other color
                    queue.append((neighbor, 1 - color, steps + 1))
        # "inf" in ans list remains when node couldn't be accessed
        # list comprehension where -1 is substituted for "inf"
        return [x if x != float("inf") else -1 for x in ans]


sol = Solution()

# n = 5
# redEdges = [[0, 2], [1, 3]]
# blueEdges = [[0, 1], [2, 4], [3, 4]]
# # Output: [0, 1, 1, 2, 2]

# n = 3
# redEdges = [[0, 1], [1, 2]]
# blueEdges = []
# # Output: [0, 1, -1]

# n = 3
# redEdges = [[0, 1]]
# blueEdges = [[2, 1]]
# # Output: [0, 1, -1]

n = 15
redEdges = [[0, 1], [0, 2], [1, 4], [2, 6], [5, 9], [7, 8], [7, 12], [9, 13], [5, 10], [3, 14]]
blueEdges = [[0, 3], [1, 5], [2, 7], [6, 11], [11, 12]]
# Output: [0, 1, 1, 1, -1, 2, -1, 2, 3, 3, 3, -1, 3, -1, 2]


print(sol.shortestAlternatingPaths(n, redEdges, blueEdges))
