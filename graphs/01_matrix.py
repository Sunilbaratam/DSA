from collections import deque

def nearestZeroDistance(mat):
    if not mat or not mat[0]:
        return []
    
    m,n = len(mat), len(mat[0])

    dist = [[float('inf')]*n for _ in range(m)]

    queue = deque()

    for i in range(m):
        for j in range(n):
            if mat[i][j]==0:
                dist[i][j] = 0
                queue.append((i,j))

    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    while queue:
        r,c = queue.popleft()

        for dr, dc in directions:
            nr,nc = r+dr, c+dc
            if 0<=nr<m and 0<=nc<n:
                if dist[nr][nc]>dist[r][c]+1:
                    dist[nr][nc] = dist[r][c]+1

                    queue.append(nr,nc)
    return dist