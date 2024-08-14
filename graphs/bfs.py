from collections import deque


#graph is the adjacency list of the graph

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    bfs_order = []

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.add(node)
            bfs_order.append(node)


            for neighbour in graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
    return bfs_order