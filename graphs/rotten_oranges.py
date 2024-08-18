from collections import deque

def rotten_oranges(graph):
    m,n = len(graph), len(graph[0])

    queue = deque()
    fresh_oranges = 0

    for i in range(m-1):
        for j in range(n-1):
            if graph[i][j]==1:
                fresh_oranges+=1
            elif graph[i][j]==2:
                queue.append((i,j))

    minutes_elapsed = 0 
    directions = [(-1,0), (1,0), (0,1), (0,-1)]
    while queue and fresh_oranges>0:
        minutes_elapsed+=1
        for _ in queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                nx,ny = x+dx, y+dy

                if 0<=nx<m and o<=ny<n and graph[nx][ny]==1:
                    graph[nx][ny]==2
                    fresh_oranges-=1
                    queue.append((nx,ny))
    
    return minutes_elapsed if fresh_oranges==0 else -1

