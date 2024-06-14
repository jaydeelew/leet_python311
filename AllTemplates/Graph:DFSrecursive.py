# build adjacency dictionary from list of edges:
# def build_graph(edges):
#     graph = defaultdict(list)
#     for x, y in edges:
#         graph[x].append(y)
#         graph[y].append(x)  # undirected version has this line
#     return graph


# def fn(graph):
#     def dfs(node):
#         ans = 0
#         # do some logic
#         for neighbor in graph[node]:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 ans += dfs(neighbor)

#         return ans

#     seen = {START_NODE}
#     return dfs(START_NODE)


def max_depth(graph, start_node):
    def dfs(node, depth):
        max_depth = depth
        for neighbor in graph[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                current_depth = dfs(neighbor, depth + 1)
                max_depth = max(max_depth, current_depth)
        return max_depth

    seen = {start_node}
    return dfs(start_node, 0)


# Example usage:
graph = {0: [1, 2], 1: [3], 2: [1], 3: []}
root = 0

# graph = {0: [1, 2], 1: [3], 2: [5], 3: [6], 5: [3, 7], 6: [], 7: []}
# root = 0
# max_depth output: 3
# max_sum_root_to_leaf output: 14

# graph = {0: [1, 4, 8], 1: [0, 2, 3, 5], 2: [1], 3: [1, 9], 4: [0, 6, 7], 5: [1], 6: [4], 7: [4], 8: [0], 9: [3]}
# root = 0
# max_depth output: 3
# max_sum_root_to_leaf output: 13

# graph = {0: []}
# root = 0
# max_depth output: 0
# max_sum_root_to_leaf output: 0

print("max_depth:", max_depth(graph, root))
