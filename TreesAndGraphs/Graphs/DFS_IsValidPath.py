# 1971. There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive).
# The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes
# a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge,
# and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination,
# or false otherwise.
from collections import defaultdict


class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        # custom exception used to unwind call stack and return True(below) w/o finishing recursion
        class valid_path(Exception):
            pass  # do nothing

        seen = {source}

        def dfs(node):
            if node == destination:
                raise valid_path  # raise exception class above
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)

        try:
            dfs(source)
            return False
        except valid_path:
            return True

    def validPath_Iterative(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        stack = [source]
        seen = set()
        while stack:
            node = stack.pop()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)
        return False


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
# return True

# n = 6
# edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
# source = 0
# destination = 5
# # return False

# n = 0
# edges = [[0, 1], [1, 2], [2, 0]]
# source = 0
# destination = 0
# # return True

sol = Solution()
print(sol.validPath(n, edges, source, destination))
print(sol.validPath_Iterative(n, edges, source, destination))
