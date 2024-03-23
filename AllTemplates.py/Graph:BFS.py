# from collections import deque

# def fn(graph):
#     queue = deque([START_NODE])
#     seen = {START_NODE}
#     ans = 0

#     while queue:
#         node = queue.popleft()
#         # do some logic
#         for neighbor in graph[node]:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 queue.append(neighbor)

#     return ans


# list the contents of each level of the BFS in order starting with root

from collections import deque


class Solution:
    def listLevels(self, graph: dict) -> list[list[int]]:
        queue = deque()
        queue.append(0)
        seen = {0}
        ans = []

        while queue:
            # do level work starting here
            ans.append(list(queue))
            level_size = len(queue)
            for _ in range(level_size):
                node = queue.popleft()
                # do node work starting here
                for neighbor in graph[node]:
                    if neighbor not in seen:
                        seen.add(neighbor)
                        queue.append(neighbor)
        return ans


sol = Solution()
# edges = [(0, 1), (0, 2), (0, 5), (1, 7), (2, 3), (2, 4), (4, 3), (3, 6), (7, 0)]  # contains a cycle

# directed (note that directed graph needs leaves to be listed as keys with no neighbors):
edges = {0: [1, 2, 5], 1: [7], 2: [3, 4], 4: [3], 3: [6], 7: [0], 5: [], 6: []}
# undirected:
# edges = {0: [1, 2, 5, 7], 1: [0, 7], 2: [0, 3, 4], 5: [0], 7: [1, 0], 3: [2, 4, 6], 4: [2, 3], 6: [3]}

print(sol.listLevels(edges))

# Output Directed Graph = [[0], [1, 2, 5], [7, 3, 4], [6]]
# Output Undirected Graph = [[0], [1, 2, 5, 7], [3, 4], [6]]
