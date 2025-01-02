# 0. Max Depth Undirected Acyclic Graph
# Given an undirected cyclic graph (in adjacency list form) and a starting node,
# return the maximum depth of the graph from starting node to a leaf.


def maxDepth(adj_list, start_node, parent=None):
    m_depth = 0

    for neighbor in adj_list[start_node]:
        if neighbor != parent:  # Only visit nodes that aren't the parent
            m_depth = max(m_depth, maxDepth(adj_list, neighbor, start_node) + 1)

    return m_depth


adj_list = {
    "a": ["b", "c", "e"],
    "b": ["a"],
    "c": ["a", "d"],
    "d": ["c"],
    "e": ["f"],
    "f": ["e", "g"],
    "g": ["f"],
}


print(maxDepth(adj_list, "a"))  # Output: 3
