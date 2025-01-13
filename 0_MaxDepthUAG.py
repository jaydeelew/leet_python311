# 0. Max Depth Undirected Acyclic Graph
# Given an undirected cyclic graph (in adjacency list form) and a starting node,
# return the maximum depth of the graph from starting node to a leaf.


def maxDepth(adj_list, node, parent=None):
    m_depth = 0

    for neighbor in adj_list[node]:
        # Only visit nodes that aren't the parent
        if neighbor != parent:
            m_depth = max(m_depth, maxDepth(adj_list, neighbor, node) + 1)

    return m_depth


# def maxDepth(adj_list, node, parent=None):
#     # if root has no children
#     if not adj_list[node]:
#         return 0
#     # if tree node
#     if len(adj_list[node]) == 1 and adj_list[node][0] == parent:
#         return 0
#     return 1 + max(maxDepth(adj_list, neighbor, node) for neighbor in adj_list[node] if neighbor != parent)


graph = {
    "a": ["b", "c", "e"],
    "b": ["a"],
    "c": ["a", "d"],
    "d": ["c"],
    "e": ["f"],
    "f": ["e", "g"],
    "g": ["f"],
}
start = "a"
print(maxDepth(graph, start))
# Output: 3

graph1 = {0: [1, 3], 1: [0, 2], 2: [1], 3: [0, 4, 5], 4: [3], 5: [3]}
start1 = 0
print(maxDepth(graph1, start1))
# Output: 2

graph2 = {0: [1], 1: [0, 2, 3, 4], 2: [1], 3: [1], 4: [1, 5], 5: [4]}
start2 = 0
print(maxDepth(graph2, start2))
# Output: 3

graph3 = {0: [1], 1: [0, 2], 2: [1, 3], 3: [2]}
start3 = 0
print(maxDepth(graph3, start3))
# Output: 3

graph4 = {0: []}
start4 = 0
print(maxDepth(graph4, start4))
# Output: 0
