# q3.py
# CS253 Assignment
# Question 3
# Name: Rajasa Lingamsetti
# Roll Number: 240596

import heapq

# Function to find shortest safe route using Dijkstra's algorithm
def find_safe_route(graph, start, end, blocked_nodes):

    n = len(graph)

    # If start or end node is blocked, no path is possible
    if start in blocked_nodes or end in blocked_nodes:
        return ([], -1)

    distances = [float("inf")] * n
    previous = [-1] * n

    distances[start] = 0

    # Priority queue stores (distance, node)
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        # Skip if this is an outdated entry
        if current_distance > distances[current_node]:
            continue

        # Explore neighbors
        for neighbor in range(n):
            weight = graph[current_node][neighbor]

            # Ignore if there is no edge or node is blocked
            if weight == 0 or neighbor in blocked_nodes:
                continue

            new_distance = current_distance + weight

            # Update shorter distance
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                previous[neighbor] = current_node
                heapq.heappush(pq, (new_distance, neighbor))

    # If destination cannot be reached
    if distances[end] == float("inf"):
        return ([], -1)

    # Reconstruct path
    path = []
    current = end

    while current != -1:
        path.append(current)
        current = previous[current]

    path.reverse()

    return (path, distances[end])


# Sample test
graph = [
    [0, 5, 0, 8, 0],
    [5, 0, 3, 0, 0],
    [0, 3, 0, 2, 7],
    [8, 0, 2, 0, 4],
    [0, 0, 7, 4, 0]
]

start_node = 0
end_node = 4
blocked = [3]

print(find_safe_route(graph, start_node, end_node, blocked))