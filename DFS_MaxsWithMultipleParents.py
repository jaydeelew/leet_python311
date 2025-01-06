# find the maximum depth of a leaf in a directed acyclic graph (DAG) from a given root
# where a node may have more that one incoming edge
def max_depth(adj_list, root):
    def dfs(node, depth):
        if depth > seen.get(node, -1):
            seen[node] = depth
            max_depth = depth
            for neighbor in adj_list[node]:
                max_depth = max(max_depth, dfs(neighbor, depth + 1))
            return max_depth
        return 0

    seen = {}
    return dfs(root, 0)


# find the maximum sum of nodes to a leaf in a directed acyclic graph (DAG) from a given root
# where a node may have more that one incoming edge
def max_sum(adj_list, root):
    def dfs(node, current_sum):
        if current_sum + node > seen.get(node, float("-inf")):
            seen[node] = current_sum + node
            max_sum = seen[node]
            if node in adj_list:
                for neighbor in adj_list[node]:
                    max_sum = max(max_sum, dfs(neighbor, seen[node]))
            return max_sum
        return 0

    seen = {}
    return dfs(root, 0)


graph = {0: [1, 2], 1: [3], 2: [1], 3: []}
root = 0
# Output: 3
# Output: 6

# graph = {0: [1, 2, 3, 8], 1: [2], 2: [3], 3: [4], 4: [], 8: [4]}
# root = 0
# Output: 4
# Output: 12

print(max_depth(graph, root))
print(max_sum(graph, root))
