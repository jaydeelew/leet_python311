# 1557. Minimum Number of Vertices to Reach All Nodes
# Given a directed acyclic graph, with n vertices numbered from 0 to n-1,
# and an array edges where edges[i] = [x, y] represents a directed edge from node x to node y.
# Find the smallest set of vertices from which all nodes in the graph are reachable.


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: list[list[int]]) -> list[int]:
        inbound = [0] * n
        for _, y in edges:
            inbound[y] += 1

        # Using Python list comprehension
        # Syntax: newList = [ expression(element) for element in oldList if condition ]
        # append n to new list if any in inbound[0 to n-1] is 0
        return [n for n in range(n) if inbound[n] == 0]


sol = Solution()
n = 6
edges = [[0, 1], [0, 2], [2, 5], [3, 4], [4, 2]]
# Output: [0, 3]

print(sol.findSmallestSetOfVertices(n, edges))
