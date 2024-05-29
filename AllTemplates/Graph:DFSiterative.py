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


# return the max depth from the root to the leaf
def max_depth(adj_list):
    stack = [[0, 0]]  # [node, depth]
    seen = {0}
    ans = 0

    while stack:
        node, depth = stack.pop()
        ans = max(ans, depth)

        for neighbor in adj_list[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append([neighbor, depth + 1])

    return ans


# return the max sum from the root to the leaf
def max_sum(adj_list):
    stack = [[0, 0]]  # [node, sum]
    seen = {0}
    ans = 0

    while stack:
        node, sum = stack.pop()
        ans = max(ans, sum)
        for neighbor in adj_list[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append([neighbor, sum + neighbor])

    return ans


# return the path to the target
def path_to_target(adj_list, target):
    stack = [(0, [0])]  # [node, path]
    seen = {0}

    while stack:
        node, curr_path = stack.pop()
        if node == target:
            return curr_path

        for neighbor in adj_list[node]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append((neighbor, curr_path + [neighbor]))


edges = {0: [2, 3], 1: [3], 2: [0], 3: [0, 1]}
target = 1
# max_depth output: 2
# max_sum_root_to_leaf output: 4
# path_to_target output: [0, 3, 1]


# edges = {0: [1, 4, 8], 1: [0, 2, 3, 5], 2: [1], 3: [1, 9], 4: [0, 6, 7], 5: [1], 6: [4], 7: [4], 8: [0], 9: [3]}
# target = 9
# max_depth output: 3
# max_sum_root_to_leaf output: 13
# path_to_target output: [0, 1, 3, 9]

# edges = {0: []}
# target = 0
# max_depth output: 0
# max_sum_root_to_leaf output: 0
# path_to_target output: [0]

print("max_depth:", max_depth(edges))
print("max_sum:", max_sum(edges))
print("path_to_target:", path_to_target(edges, target))
