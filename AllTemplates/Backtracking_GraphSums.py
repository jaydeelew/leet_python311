def max_depth(adj_list, start_node):
    # must declare max_depth before dfs is read into memory
    # since nonlocal will check to see if max_sum was defined above in the outer scope
    max_depth = 0

    def backtrack(curr_node, curr_path, curr_depth):
        nonlocal max_depth

        for neighbor, dist in adj_list[curr_node].items():
            if neighbor not in curr_path:
                new_depth = curr_depth + 1
                max_depth = max(max_depth, new_depth)
                curr_path.append(neighbor)
                backtrack(neighbor, curr_path, new_depth)
                curr_path.pop()

    backtrack(start_node, [start_node], 0)
    return max_depth


def max_sum(adj_list, start_node):
    # must declare max_sum before dfs is read into memory
    # since nonlocal will check to see if max_sum was defined above in the outer scope
    max_sum = 0

    def backtrack(curr_node, curr_path, curr_sum):
        nonlocal max_sum

        for neighbor, dist in adj_list[curr_node].items():
            if neighbor not in curr_path:
                new_sum = curr_sum + dist
                max_sum = max(max_sum, new_sum)
                curr_path.append(neighbor)
                backtrack(neighbor, curr_path, new_sum)
                curr_path.pop()

    backtrack(start_node, [start_node], 0)
    return max_sum


adj_list = {
    "a": {"b": 1, "c": 2},
    "b": {"a": 1, "c": 3, "d": 4},
    "c": {"a": 2, "b": 3, "d": 6},
    "d": {"b": 4, "c": 6},
}

adj_list_2 = {
    "p": {"q": 7, "r": 3, "s": 2},
    "q": {"p": 7, "t": 4, "u": 1},
    "r": {"p": 3, "v": 5, "x": 3},
    "s": {"p": 2, "w": 6, "x": 2},
    "t": {"q": 4, "u": 3},
    "u": {"q": 1, "t": 3},
    "v": {"r": 5, "w": 4},
    "w": {"s": 6, "v": 4},
    "x": {"r": 3, "x": 2},
}

print(max_depth(adj_list, "a"))  # Output: 3
print(max_sum(adj_list, "a"))  # Output: 12

print(max_depth(adj_list_2, "p"))  # Output: 3
print(max_sum(adj_list_2, "p"))  # Output: 18
