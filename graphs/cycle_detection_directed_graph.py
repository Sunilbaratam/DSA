def isCyclic(graph):
    def dfs(node):
        visited[node] = True
        recStack[node] = True
        
        # Explore all adjacent nodes
        for neighbor in graph[node]:
            if not visited[neighbor]:  # If neighbor hasn't been visited, recurse on it
                if dfs(neighbor):
                    return True
            elif recStack[neighbor]:  # If neighbor is in the recursion stack, a cycle is detected
                return True
        
        recStack[node] = False  # Remove the node from recursion stack before backtracking
        return False
    
    num_nodes = len(graph)
    visited = [False] * num_nodes
    recStack = [False] * num_nodes
    
    # Check for cycles in each component of the graph
    for node in range(num_nodes):
        if not visited[node]:
            if dfs(node):
                return True
    
    return False
