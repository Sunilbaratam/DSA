from collections import deque

def isBipartite(graph):
    n = len(graph)
    color = [-1] * n  # -1 means uncolored, 0 and 1 are the two colors
    
    def bfs(start):
        queue = deque([start])
        color[start] = 0  # Start coloring with 0
        
        while queue:
            node = queue.popleft()
            current_color = color[node]
            for neighbor in graph[node]:
                if color[neighbor] == -1:  # If the neighbor is uncolored
                    color[neighbor] = 1 - current_color  # Color it with the opposite color
                    queue.append(neighbor)
                elif color[neighbor] == current_color:  # If the neighbor has the same color
                    return False
        
        return True
    
    for i in range(n):
        if color[i] == -1:  # If the vertex is uncolored, start a BFS
            if not bfs(i):
                return False
    
    return True
