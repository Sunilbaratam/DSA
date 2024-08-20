from collections import deque

def topological_sort_kahn(graph, num_vertices):
    in_degree = [0] * num_vertices
    for v in range(num_vertices):
        for neighbor in graph[v]:
            in_degree[neighbor] += 1

    queue = deque([v for v in range(num_vertices) if in_degree[v] == 0])
    topo_order = []

    while queue:
        v = queue.popleft()
        topo_order.append(v)

        for neighbor in graph[v]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(topo_order) == num_vertices:
        return topo_order
    else:
        raise ValueError("Graph has a cycle and therefore no topological sort exists")
