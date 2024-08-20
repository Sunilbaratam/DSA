from collections import deque, defaultdict

def has_cycle(graph, num_vertices):
    # Step 1: Calculate in-degree of each vertex
    in_degree = [0] * num_vertices
    for u in range(num_vertices):
        for v in graph[u]:
            in_degree[v] += 1

    # Step 2: Initialize a queue with all vertices having in-degree of zero
    queue = deque([v for v in range(num_vertices) if in_degree[v] == 0])

    # Step 3: Process the vertices
    count = 0
    while queue:
        u = queue.popleft()
        count += 1  # Increment the count of processed vertices

        # For each adjacent vertex, reduce its in-degree by 1
        for v in graph[u]:
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    # Step 4: Check for cycle
    # If the count of processed vertices is less than the total number of vertices, there's a cycle
    return count != num_vertices

# Example Usage
graph = {
    0: [1, 2],
    1: [2],
    2: [3],
    3: [1],
    4: [5],
    5: [],
}
num_vertices = 6

if has_cycle(graph, num_vertices):
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")
