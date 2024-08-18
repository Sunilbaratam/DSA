from collections import deque

def isCyclic(graph, V):
    visited = [False] * V
    
    def bfs(start):
        queue = deque([(start, -1)])  # (current node, parent node)
        visited[start] = True
        
        while queue:
            node, parent = queue.popleft()
            
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append((neighbor, node))
                elif neighbor != parent:
                    return True
        
        return False
    
    for i in range(V):
        if not visited[i]:
            if bfs(i):
                return True
    
    return False
