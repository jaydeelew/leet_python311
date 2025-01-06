# 2368. There is an undirected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.
# You are given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is
# an edge between nodes ai and bi in the tree. You are also given an integer array restricted which represents restricted nodes.
# Return the maximum number of nodes you can reach from node 0 without visiting a restricted node.
# Note that node 0 will not be a restricted node.
from collections import defaultdict


class Solution:
    def reachableNodes(self, n: int, edges: list[list[int]], restricted: list[int]) -> int:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        seen = {0}  # the initial node
        restricted_nodes = set(restricted)

        def dfs(node):
            ans = 0
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    if neighbor not in restricted_nodes:
                        ans += dfs(neighbor) + 1
            return ans

        return dfs(0) + 1  # plus one for node 0


n = 7
edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
restricted = [4, 5]  # output: 4

# n = 7
# edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
# restricted = [4, 2, 1]  # output: 3

sol = Solution()
print(sol.reachableNodes(n, edges, restricted))
