# 0. List Graph Levels
# Given a directed or undirected graph in the form of an adjacency list,
# return a list of lists of elements at each level.
from collections import deque


def listLevels(adj_list, root):
    queue = deque([root])
    seen = {root}
    ans = []

    while queue:
        # do level work here
        ans.append(list(queue))

        level_size = len(queue)
        for _ in range(level_size):
            node = queue.popleft()
            # do node work here

            for neighbor in adj_list[node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

    return ans


def list_levels_INCORRECT(adj_list, root):
    queue = deque([root])
    seen = set()
    ans = []

    while queue:
        ans.append(list(queue))
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()
            if node not in seen:
                seen.add(node)
            # if we check for seen when popping off the queue, as we did here,
            # we potentially add already seen nodes back onto the queue which could lead to an endless loop
            # or duplicate nodes on a level
            for neighbor in adj_list[node]:
                queue.append(neighbor)

    return ans


# note that directed graph needs leaves to be listed as keys with no neighbors
directed = {0: [1, 2, 5], 1: [7], 2: [3, 4], 4: [3], 3: [6], 7: [0], 5: [], 6: []}
# Output Directed Graph = [[0], [1, 2, 5], [7, 3, 4], [6]]
undirected = {0: [1, 2, 5, 7], 1: [0, 7], 2: [0, 3, 4], 5: [0], 7: [1, 0], 3: [2, 4, 6], 4: [2, 3], 6: [3]}
# Output Undirected Graph = [[0], [1, 2, 5, 7], [3, 4], [6]]

print(listLevels(directed, 0))
print(listLevels(undirected, 0))
