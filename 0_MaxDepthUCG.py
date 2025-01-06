# 0. Max Depth Undirected Cyclic Graph
# Given an undirected cyclic graph (in adjacency list form) and a starting node,
# return the maximum depth of the graph from starting node to a leaf.


def maxDepth(adj_list, start_node):
    def dfs(node, seen):
        m_depth = 0
        seen.add(node)  # Mark current node as seen

        for neighbor in adj_list[node]:
            if neighbor not in seen:  # Only visit unseen neighbors
                m_depth = max(m_depth, dfs(neighbor, seen) + 1)

        seen.remove(node)  # Backtrack: remove node from seen set
        return m_depth

    return dfs(start_node, set())


adj_list = {
    "a": ["b", "c"],
    "b": ["a", "c", "d"],
    "c": ["a", "b", "d"],
    "d": ["b", "c"],
}

adj_list_2 = {
    "p": ["q", "s", "r"],
    "q": ["p", "t", "u"],
    "r": ["p", "v", "x"],
    "s": ["p", "w", "x"],
    "t": ["q", "u"],
    "u": ["q", "t"],
    "v": ["r", "w"],
    "w": ["s", "v"],
    "x": ["r", "s"],
}

print(maxDepth(adj_list, "a"))  # Output: 3
print(maxDepth(adj_list_2, "p"))  # Output: 5
