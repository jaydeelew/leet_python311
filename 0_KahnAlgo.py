# 0. Kahn's Algorithm
# Given a directed adj_list in the form an adjacency list, return a array of the topological ordering of the nodes.
# If this is not possible, return None.
from collections import deque


def khan(adj_list):
    ans = []
    q = deque()

    indegree = {node: 0 for node in adj_list}  # dict
    for node in adj_list:
        for neighbor in adj_list[node]:
            indegree[neighbor] += 1

    for node in indegree:
        if indegree[node] == 0:
            q.append(node)

    while len(q) > 0:
        node = q.popleft()
        ans.append(node)

        for neighbor in adj_list[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                q.append(neighbor)

    return ans if len(adj_list) == len(ans) else None


adj_list = {1: [], 2: [1], 3: [1], 4: [2], 5: [2], 6: [3]}
# Output: [4, 5, 6, 2, 3, 1]

# adj_list = {2: [1], 3: [1, 5], 4: [2], 5: [2, 6], 6: [3], 1: []}  # has cycle
# Output: None

print(khan(adj_list))
