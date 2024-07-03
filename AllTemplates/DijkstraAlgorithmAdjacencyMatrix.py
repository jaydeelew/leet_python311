import heapq


def dijkstra(adj_matrix, starting_node):
    # distances maintains the shortest distance from the starting node to all other vertices
    # distances = dict.fromkeys(range(len(adj_matrix)), float("inf"))
    distances = {node: float("inf") for node in range(len(adj_matrix))}
    distances[starting_node] = 0

    # list of tuples: (current minimum distance from start, current node)
    min_heap = [(0, starting_node)]
    # seen is needed to prevent revisiting nodes that already have their shortest distance from start computed
    seen = set()

    while min_heap:
        # we use a min heap here instead of a FIFO queue to potentially reduce
        # the number of times we update the distance of a node
        dist_from_start, node = heapq.heappop(min_heap)

        if node not in seen:
            # a seen neighbor's distance from start can still
            # be updated in distances by the current node
            seen.add(node)
            # for each neighbor of the current node, we calculate the distance from start to neighbor
            for neighbor in range(len(adj_matrix)):
                if adj_matrix[node][neighbor] > 0:  # Dijstra's does not allow for negative weights
                    dist_to_neighbor = adj_matrix[node][neighbor]
                    dist_start_to_neighbor = dist_from_start + dist_to_neighbor

                    # if the distance from start neighbor is shorter than the total distance recorded thus far,
                    # we update the distance for our neighbor in distances and push the neighbor onto the heap
                    if dist_start_to_neighbor < distances[neighbor]:
                        distances[neighbor] = dist_start_to_neighbor
                        heapq.heappush(min_heap, (dist_start_to_neighbor, neighbor))

    return distances


adj_matrix = [
    [0, 8, 4, 0, 0],
    [0, 0, 4, 0, 0],
    [0, 3, 0, 2, 5],
    [0, 0, 0, 0, 2],
    [0, 0, 0, 0, 0],
]

print(dijkstra(adj_matrix, 0))
# Output: {0: 0, 1: 7, 2: 4, 3: 6, 4: 8}
