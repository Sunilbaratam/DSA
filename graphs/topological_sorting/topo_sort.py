# v is the no of vertices
def topological_sorting(graph, v):

    def dfs(node, visited):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour, visited)

        stack.append(node)
    
    visited = set()

    stack = []

    for i in range(v):
        if i not in visited:
            dfs(v)

    return stack[::-1]