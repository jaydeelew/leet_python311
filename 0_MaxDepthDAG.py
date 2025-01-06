# 0. Max Depth DAG
# Given a directed acyclic graph (in adjacency list form) and a starting node,
# return the maximum depth of the graph from starting node to a leaf.


def max_depth(adj_list, start_node):
    def dfs(node):
        m_depth = 0

        for neighbor in adj_list[node]:
            # the plus one counts the edge to the neighbor
            m_depth = max(m_depth, dfs(neighbor) + 1)

        return m_depth

    return dfs(start_node)


# adj_list = {0: [2, 3], 1: [], 2: [], 3: [1]}
# start = 0
# Output: 2

adj_list = {0: [1, 3], 1: [2], 2: [6], 3: [4, 5], 4: [], 5: [], 6: []}
start = 0
# Output: 3

print(max_depth(adj_list, start))
