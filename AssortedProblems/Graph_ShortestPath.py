# Given a network of friends in the form of an adjacency list, return the shortest path between two people
from collections import deque


# the recontructs the path from start node to end node by traversing through to-neighbor from-node and
# then reversing the list
def build_path(neighbor_node, start, end):
    path = []

    node = end
    while node:
        path.append(node)
        node = neighbor_node[node]

    path.reverse()
    return path


# this version checks if a node had been visited before adding it to the queue
def shortest_path(adj_list, start, end):
    queue = deque([start])
    # neighbor node is a dictionary where key is the neighbor and the value is the node
    # when we reconstruct the path with build_path() above, the while loop is terminated when node = None,
    # hence we add start:None
    neighbor_node = {start: None}

    while queue:
        node = queue.popleft()

        if node == end:
            return build_path(neighbor_node, start, end)

        for neighbor in adj_list[node]:
            # neighbor node also acts as seen/visited
            if neighbor not in neighbor_node:
                queue.append(neighbor)
                neighbor_node[neighbor] = node

    return None


# this version checks if a node had been visited after popping it from the queue
# and can allow for already visited nodes to be enqueued which can be less efficient
def shortest_path_2(adj_list, start, end):
    queue = deque([start])
    neighbor_node = {start: None}

    while queue:
        node = queue.popleft()
        if node not in neighbor_node:
            if node == end:
                return build_path(neighbor_node, start, end)

            for neighbor in adj_list[node]:
                queue.append(neighbor)
                neighbor_node[neighbor] = node

    return None


network = {
    "Min": ["William", "Jayden", "Omar"],
    "William": ["Min", "Noam"],
    "Jayden": ["Min", "Amelia", "Ren", "Noam"],
    "Ren": ["Jayden", "Omar"],
    "Amelia": ["Jayden", "Adam", "Miguel"],
    "Adam": ["Amelia", "Miguel", "Sofia", "Lucas"],
    "Miguel": ["Amelia", "Adam", "Liam", "Nathan"],
    "Noam": ["Nathan", "Jayden", "William"],
    "Omar": ["Ren", "Min", "Scott"],
}
# Output:  ['Jayden', 'Amelia', 'Adam']

print(shortest_path(network, "Jayden", "Adam"))
print(shortest_path(network, "Jayden", "Adam"))
