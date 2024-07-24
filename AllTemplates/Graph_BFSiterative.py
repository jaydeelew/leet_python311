# build adjacency dictionary from list of edges:
# def build_graph(edges):
#     graph = defaultdict(list)
#     for x, y in edges:
#         graph[x].append(y)
#         graph[y].append(x)  # undirected version has this line
#     return graph


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


# list the contents of each level of the graph (in adjacency list form) using BFS (iteratively) starting with root
from collections import defaultdict, deque


def list_levels(adj_list, root):
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


def build_directed_graph(edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
    return graph


def build_undirected_graph(edges):
    graph = defaultdict(list)
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)  # undirected version has this line
    return graph


edges = [(0, 1), (0, 2), (0, 5), (1, 7), (2, 3), (2, 4), (4, 3), (3, 6), (7, 0)]  # contains a cycle

# note that directed graph needs leaves to be listed as keys with no neighbors
# directed = {0: [1, 2, 5], 1: [7], 2: [3, 4], 4: [3], 3: [6], 7: [0], 5: [], 6: []}
# undirected = {0: [1, 2, 5, 7], 1: [0, 7], 2: [0, 3, 4], 5: [0], 7: [1, 0], 3: [2, 4, 6], 4: [2, 3], 6: [3]}

directed = build_directed_graph(edges)
undirected = build_undirected_graph(edges)

print(list_levels(directed, 0))
print(list_levels(undirected, 0))

# Output Directed Graph = [[0], [1, 2, 5], [7, 3, 4], [6]]
# Output Undirected Graph = [[0], [1, 2, 5, 7], [3, 4], [6]]
