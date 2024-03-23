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


def max_depth(graph):
    stack = [[0, 0]]  # [node, depth]
    seen = {0}
    ans = 0
    curr_depth = 0

    while stack:
        node = stack.pop()
        ans = max(ans, node[1])
        for neighbor in graph[node[0]]:
            if neighbor not in seen:
                seen.add(neighbor)
                curr_depth = node[1] + 1
                stack.append([neighbor, curr_depth])

    return ans


def max_sum_root_to_leaf(graph):
    stack = [[0, 0]]  # [node, sum]
    seen = {0}
    ans = 0
    curr_sum = 0

    while stack:
        node = stack.pop()
        ans = max(ans, node[1])
        for neighbor in graph[node[0]]:
            if neighbor not in seen:
                seen.add(neighbor)
                curr_sum = node[1] + neighbor
                stack.append([neighbor, curr_sum])

    return ans


# edges is an adjacency list

edges = [[2, 3], [3], [0], [0, 1]]
# max_depth output: 2
# max_sum_root_to_leaf output: 2


# edges = [[1, 4, 8], [0, 2, 3, 5], [1], [1, 9], [0, 6, 7], [1], [4], [4], [0], [3]]
# max_depth output: 3
# max_sum_root_to_leaf output: 13

# edges = [[]]
# max_depth output: 0
# max_sum_root_to_leaf output: 0


print(max_depth(edges))
print(max_sum_root_to_leaf(edges))
