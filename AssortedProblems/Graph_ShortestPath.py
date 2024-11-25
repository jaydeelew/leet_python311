# Given a network of friends in the form of an adjacency list, return the shortest path between two people
from collections import deque


def shortest_path(adj_list, start, end):
    queue = deque([start])
    seen = set()
    # dictionary where key is the last element in the tuple of path from start node to current neighbor
    paths_dict = {start: [start]}

    while queue:
        sz = len(queue)

        for _ in range(sz):
            node = queue.popleft()

            if node not in seen:
                seen.add(node)
                # dictionary pop removes the key:value pair and return the value
                path_ending_in_node = paths_dict.pop(node)

                for neighbor in adj_list[node]:
                    new_path = path_ending_in_node + [neighbor]

                    if neighbor == end:
                        return new_path
                    else:
                        queue.append(neighbor)
                        paths_dict[neighbor] = new_path


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
