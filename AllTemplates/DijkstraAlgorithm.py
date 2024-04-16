# import heapq
import heapq


def calculate_distances(graph, starting_vertex):
    # distances maintains the shortest distance from the starting vertex to all other vertices
    distances = {vertex: float("inf") for vertex in graph}
    distances[starting_vertex] = 0

    # list of tuples: (current distance, current vertex)
    min_heap = [(0, starting_vertex)]

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)

        # if the current distance is greater than the distance already computed for the current vertex,
        # then we have already found a shorter path to the current vertex
        # so we can skip this iteration
        if current_distance > distances[current_vertex]:
            continue

        # for each neighbor of the current vertex, we calculate the distance to the neighbor
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # if the distance to the neighbor is shorter than the current distance,
            # we update the distance in distances and push the neighbor into the heap
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances


example_graph = {
    "U": {"V": 2, "W": 5, "X": 1},
    "V": {"U": 2, "X": 2, "W": 3},
    "W": {"V": 3, "U": 5, "X": 3, "Y": 1, "Z": 5},
    "X": {"U": 1, "V": 2, "W": 3, "Y": 1},
    "Y": {"X": 1, "W": 1, "Z": 1},
    "Z": {"W": 5, "Y": 1},
}

print(calculate_distances(example_graph, "U"))
