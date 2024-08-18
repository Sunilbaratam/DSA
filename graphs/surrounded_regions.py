from collections import deque

def captureSurroundedRegions(board):
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    
    # Directions for moving in the grid (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    def bfs(r, c):
        queue = deque([(r, c)])
        board[r][c] = '#'
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = '#'
                    queue.append((nr, nc))
    
    # Mark all 'O's on the border and connected to the border as safe '#'
    for i in range(m):
        if board[i][0] == 'O':
            bfs(i, 0)
        if board[i][n - 1] == 'O':
            bfs(i, n - 1)
    
    for j in range(n):
        if board[0][j] == 'O':
            bfs(0, j)
        if board[m - 1][j] == 'O':
            bfs(m - 1, j)
    
    # Capture all surrounded regions by converting 'O' to 'X'
    # and revert the safe regions marked with '#' back to 'O'
    for i in range(m):
        for j in range(n):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == '#':
                board[i][j] = 'O'

    return board
