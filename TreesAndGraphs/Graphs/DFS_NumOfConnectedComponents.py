# 323. You have a graph of n nodes. You are given an integer n and an array edges
# where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.
# Return the number of connected components in the graph.
from collections import defaultdict


class Solution:
    def countComponents(self, n: int, edges: list[list[int]]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = set()

        # this adds to seen all nodes (neighbors) connected to node
        def dfs(node):
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        ans = 0

        for node in range(n):
            if node not in seen:
                seen.add(node)
                ans += 1
                dfs(node)

        return ans


# n = 5
# edges = [[0, 1], [1, 2], [3, 4]] # output 2

n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]  # output 1

sol = Solution()
print(sol.countComponents(n, edges))
