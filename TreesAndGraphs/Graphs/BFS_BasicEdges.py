from collections import deque
from collections import defaultdict


class Solution:
    def listLevels(self, edges: list[tuple]) -> list[list[int]]:
        graph = defaultdict(list)
        # build graph
        for x, y in edges:
            graph[x].append(y)
            # graph[y].append(x)  # uncomment for undirected graph

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
edges = [(0, 1), (0, 2), (0, 5), (1, 7), (2, 3), (2, 4), (4, 3), (3, 6), (7, 0)]  # contains a cycle
print(sol.listLevels(edges))

# Output Directed Graph = [[0], [1, 2, 5], [7, 3, 4], [6]]
# Output Undirected Graph = [[0], [1, 2, 5, 7], [3, 4], [6]]
