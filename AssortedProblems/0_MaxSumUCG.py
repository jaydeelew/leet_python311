# 0. Max Sum Undirected Cyclic Graph
# Given an undirected cyclical graph and a starting node, return the maximum distance from the starting
# node going through all other nodes and not visiting any node more than once.


# This version makes use of nonlocal to keep track of the max sum.
def maxSum(adj_list, start_node):
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


# This version's backtrack function returns the max sum.
def maxSum2(adj_list, start_node):

    def backtrack(curr_node, curr_path, curr_sum):
        max_sum = curr_sum

        for neighbor, dist in adj_list[curr_node].items():
            if neighbor not in curr_path:
                curr_path.append(neighbor)
                new_sum = curr_sum + dist
                max_sum = max(max_sum, backtrack(neighbor, curr_path, new_sum))
                curr_path.pop()

        return max_sum

    return backtrack(start_node, [start_node], 0)


def maxSum3(adj_list, start_node):
    # Convert node names to indices for bit manipulation
    nodes = list(adj_list.keys())
    node_to_idx = {node: i for i, node in enumerate(nodes)}

    # Create DP table: (current_node, visited_mask) -> max_sum
    dp = {}

    def solve(curr_node, visited):
        # If we've seen this state before, return cached result
        state = (curr_node, visited)
        if state in dp:
            return dp[state]

        max_sum = 0

        # Try visiting each unvisited neighbor
        for neighbor, dist in adj_list[curr_node].items():
            neighbor_idx = node_to_idx[neighbor]
            if not (visited & (1 << neighbor_idx)):  # if neighbor not visited
                # Mark neighbor as visited using bitmask
                new_visited = visited | (1 << neighbor_idx)
                new_sum = dist + solve(neighbor, new_visited)
                max_sum = max(max_sum, new_sum)

        dp[state] = max_sum
        return max_sum

    # Start with only start_node visited
    initial_visited = 1 << node_to_idx[start_node]
    return solve(start_node, initial_visited)


adj_list = {
    "a": {"b": 1, "c": 2},
    "b": {"a": 1, "c": 3, "d": 4},
    "c": {"a": 2, "b": 3, "d": 6},
    "d": {"b": 4, "c": 6},
}

adj_list_2 = {
    "p": {"q": 7, "r": 3, "s": 2},
    "q": {"p": 7, "t": 4, "u": 1},
    "r": {"p": 3, "v": 5, "x": 2},
    "s": {"p": 2, "w": 6, "x": 2},
    "t": {"q": 4, "u": 3},
    "u": {"q": 1, "t": 3},
    "v": {"r": 5, "w": 4},
    "w": {"s": 6, "v": 4},
    "x": {"r": 2, "s": 2},
}

print(maxSum(adj_list, "a"))  # Output: 12
print(maxSum(adj_list_2, "p"))  # Output: 20

print(maxSum2(adj_list, "a"))  # Output: 12
print(maxSum2(adj_list_2, "p"))  # Output: 20

print(maxSum3(adj_list, "a"))  # Output: 12
print(maxSum3(adj_list_2, "p"))  # Output: 20
