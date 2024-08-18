def iscyclic(graph, V):
    visited = [False]*V

    def dfs(v, parent):
        visited[v] = True

        for each in graph[v]:
            if not visited[each]:
                if dfs(each, v):
                    return True
            elif parent != each:
                return True
        return False
    
    for i in range(V):
        if not visited[i]:
            if dfs(i,-1):
                return True
    return False