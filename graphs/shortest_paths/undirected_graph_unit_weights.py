from collections import defaultdict, deque

class Solution:
    def shortestPath(self, edges, n, m, src):
        # code here
        
        adj=[[] for _ in range(n)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        q=deque()
        visited=[False]*n
        q.append(src)
        visited[src]=True
        distance=[-1]*n
        level=0
        while q:
            for _ in range(len(q)):
                u=q.popleft()
                distance[u]=level
                for v in adj[u]:
                    if visited[v]==False:
                        q.append(v)
                        visited[v]=True
            level+=1
        return distance
    

    from collections import deque

def bfs_shortest_path(graph, start, target):
    # Initialize the queue for BFS
    queue = deque([start])
    
    # Initialize a dictionary to track visited nodes and their distances
    distances = {start: 0}
    visited = set([start])
    
    while queue:
        node = queue.popleft()
        
        # If the target is found, return the distance
        if node == target:
            return distances[node]
        
        # Traverse neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)  # Mark as visited
                distances[neighbor] = distances[node] + 1
                queue.append(neighbor)
    
    return -1  # Return -1 if the target is not reachable

# Example graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Find the shortest path from A to F
print(bfs_shortest_path(graph, 'A', 'F'))  # Output: 2
