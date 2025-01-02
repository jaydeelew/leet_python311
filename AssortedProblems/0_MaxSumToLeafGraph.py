# 0. Max Sum to Leaf in a Graph
# Given a directed acyclic graph (in adjacency list form) and a starting node,
# return the maximum sum of the graph from starting node to a leaf.


def maxSumToLeaf(adj_list, start_node):
    def dfs(node):
        # max_sum starts at 0 for each call to dfs since below the max sum
        # of all neighbors will be evaluated and then added to the value of this node
        max_sum = 0

        for neighbor in adj_list[node]:
            max_sum = max(max_sum, dfs(neighbor))

        # return the maximum sum returned from all the neighbors plus the value of this node
        return max_sum + node

    return dfs(start_node)


graph = {0: [1, 3], 1: [2], 2: [], 3: [4, 5], 4: [], 5: []}
start = 0
print(maxSumToLeaf(graph, start))
# Output: 8

graph2 = {0: [1], 1: [2, 3, 4], 2: [], 3: [], 4: [5], 5: []}
start2 = 0
print(maxSumToLeaf(graph2, start2))
# Output: 10

graph3 = {0: [1], 1: [2], 2: [3], 3: []}
start3 = 0
print(maxSumToLeaf(graph3, start3))
# Output: 6

graph4 = {0: []}
start4 = 0
print(maxSumToLeaf(graph4, start4))
# Output: 0
