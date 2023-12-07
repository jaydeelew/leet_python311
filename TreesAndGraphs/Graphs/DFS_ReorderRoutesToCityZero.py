# 1466. Reorder Routes to Make All Paths Lead to the City Zero
# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel
# between two different cities.
# Roads are represented by connections where connections[i] = [x, y] represents a road from city x to city y.
# The edges are directed. You need to swap the direction of some edges so that every city can reach city 0.
# Return the minimum number of swaps needed.
from collections import defaultdict


class Solution:
    def minReorder(self, connections: list[list[int]]) -> int:
        # roads is the same group of directed eges from connections in set format for O(1) access time
        roads = set()
        # build undirected graph from set of directed edges in connections
        graph = defaultdict(list)
        for x, y in connections:
            graph[x].append(y)
            graph[y].append(x)
            # build roads
            roads.add((x, y))

        def dfs(node):
            ans = 0
            # for each value (neighbor) in undirected dictionary named graph
            for neighbor in graph[node]:
                # since we are dealing with an undirected graph (two directional entries per edge),
                # if we do not add neighbor to seen, we end up with infinite recursion
                # if neighbor was seen, this base case will not call dfs again
                if neighbor not in seen:
                    # since we are starting at origin 0 and moving away toward neighbors in undirected graph,
                    # if exists directed edge (road) pointing away from origin 0,
                    if (node, neighbor) in roads:
                        # the road is pointing away from 0 and needs to flip direction
                        ans += 1
                    seen.add(neighbor)
                    # each call to dfs will return 0 or 1 depending if directed edge is pointing away from 0
                    ans += dfs(neighbor)

            return ans

        seen = {0}  # add 0 to seen since it's the origin and only neighbor will be added later
        return dfs(0)


connections = [[0, 1], [2, 3], [3, 1], [4, 0], [5, 4]]  # output: 1
# connections = [[1, 0], [1, 2], [3, 2], [3, 4]]  # output: 2
# connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]  # output: 3

sol = Solution()
print(sol.minReorder(connections))
