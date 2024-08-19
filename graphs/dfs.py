
# Recursive DFS
# Graph is the adj.list of that given graph

def dfsOfGraph(self, V, adj):
        dfs_list = []
    
        def dfs(v, visited):
            visited.add(v)
            dfs_list.append(v)
            
            for neighbour in adj[v]:
                if neighbour not in visited:
                    dfs(neighbour, visited)
        
        visited = set()
        dfs(0, visited)  # Start DFS from vertex 0
        
        return dfs_list



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

