
# Recursive DFS
# Graph is the adj.list of that given graph

dfs_list = []
def recursive_dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(node)
    dfs_list.append(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            recursive_dfs(graph, neighbour, visited)


# Iterative DFS
# Graph is the adj.list of that given graph

def iterative_dfs(graph, start):
    visited = set()
    stack = [start]
    dfs_order = []

    while stack:
        node = stack.pop()

        if node not in visited:
            visited.add(node)
            dfs_order.append(node)
        
        for neighbour in reversed(graph[node]):
            if neighbour not in visited:
                stack.append(neighbour)
    return dfs_order

