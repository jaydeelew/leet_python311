# 547. Number of Provinces
# There are n cities. A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix "isConnected" where isConnected[i][j] = isConnected[j][i] = 1 if the
# ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise. Return the total number of provinces.
from collections import defaultdict


class Solution:
    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        # a recursive function that takes an int as key to a graph which is a dict of city-keys each w/ list of neighbor-values
        def dfs(node):  # node here is an integer
            for neighbor in graph[node]:  # node is the key in the graph dictionary which references a list of neighbor nodes
                # add neighbors of this node, if not present in seen set, to avoid incrementing ans below for a province
                if neighbor not in seen:
                    seen.add(neighbor)
                    dfs(neighbor)  # call dfs on each neighbor of this node

        def dfs_iterative(start_node):
            stack = [start_node]
            while stack:
                node = stack.pop()
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        stack.append(neighbor)

        # build the graph
        n = len(isConnected)  # for as many rows in "isConnected" (a dictionary of lists of neighbors)
        graph = defaultdict(list)  # defaultdict allows us to append values to keys that do not yet exist. They will be created.
        for i in range(n):
            for j in range(i + 1, n):  # main diagonal and values below it are ignored
                if isConnected[i][j]:  # if result is 1
                    graph[i].append(j)  # above main diagonal
                    graph[j].append(i)  # below main diagonal (since undirected graph includes mirror entry)

        seen = set()
        ans = 0

        # for each city, if not in seen, increment num of provinces then add city to seen, run dfs to add its neighbors to seen
        for i in range(n):  # for as many rows in "isConnected" (a dictionary of lists of neighbors)
            if i not in seen:  # node i has not yet had a dfs run on it thereby adding all of its neighbors to seen
                ans += 1  # add another province
                seen.add(i)
                dfs(i)  # add all of this node's neighbors to seen via dfs()

        return ans


# adjacency matrices
# adj_matrix = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]  # returns 2. undirected edges: [0,3], [1,2]
# adj_matrix = [[0, 0, 1, 1], [0, 0, 1, 0], [1, 1, 0, 0], [1, 0, 0, 0]]  # returns 1. undirected edges: [0,3], [1,2], [2,0]
adj_matrix = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]  # returns 3. undirected edges: [0,0], [1,1], [2,2] (three one-city provinces)
sol = Solution()
print(sol.findCircleNum(adj_matrix))
