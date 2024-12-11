# Given a network of friends in the form of an adjacency list, return the shortest path between two people
from collections import deque


# using a deque here is more efficient in adding to the front of the queue in O(1) time as opposed to
# building the path with a list and append, and the having to reverse the list.
def build_path(neighbor_node, end):
    path = deque([])
    node = end

    while node:
        path.appendleft(node)
        node = neighbor_node[node]

    return list(path)


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
            return build_path(neighbor_node, end)

        for neighbor in adj_list[node]:
            # neighbor node also acts as seen/visited
            if neighbor not in neighbor_node:
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
