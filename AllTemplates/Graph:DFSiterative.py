# def fn(graph):
#     stack = [START_NODE]
#     seen = {START_NODE}
#     ans = 0

#     while stack:
#         node = stack.pop()
#         # do some logic
#         for neighbor in graph[node]:
#             if neighbor not in seen:
#                 seen.add(neighbor)
#                 stack.append(neighbor)

#     return ans


# return the max depth of a graph (in adjacency list form) from root to leaf
def max_depth(adj_list, root):
    stack = [[root, 0]]  # node, depth
    seen = {root}
    ans = 0

    while stack:
        node, depth = stack.pop()
        ans = max(ans, depth)

        # for neighbor in adj_list[node]:
        for i in range(len(adj_list[node]) - 1, -1, -1):
            neighbor = adj_list[node][i]
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append([neighbor, depth + 1])

    return ans


# return the max sum in a graph (in adjacency list form) from root to leaf
def max_sum(adj_list, root):
    stack = [[root, root]]  # node, sum
    seen = {root}
    ans = 0

    while stack:
        node, sum = stack.pop()
        ans = max(ans, sum)
        for i in range(len(adj_list[node]) - 1, -1, -1):
            neighbor = adj_list[node][i]
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append([neighbor, sum + neighbor])

    return ans


graph = {0: [1, 2], 1: [3], 2: [5], 3: [6], 5: [3, 7], 6: [], 7: []}
# max_depth output: 3
# max_sum_root_to_leaf output: 14


# graph = {0: [1, 4, 8], 1: [0, 2, 3, 5], 2: [1], 3: [1, 9], 4: [0, 6, 7], 5: [1], 6: [4], 7: [4], 8: [0], 9: [3]}
# max_depth output: 3
# max_sum_root_to_leaf output: 13

# graph = {0: []}
# max_depth output: 0
# max_sum_root_to_leaf output: 0

print("max_depth:", max_depth(graph, 0))
print("max_sum:", max_sum(graph, 0))
