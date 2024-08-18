def numEnclaves(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
            return
        grid[r][c] = 0  # Mark the cell as visited (safe)
        # Explore all 4 directions
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right
    
    # Mark all the land cells connected to the boundary as safe
    for i in range(m):
        if grid[i][0] == 1:  # Left boundary
            dfs(i, 0)
        if grid[i][n - 1] == 1:  # Right boundary
            dfs(i, n - 1)
    
    for j in range(n):
        if grid[0][j] == 1:  # Top boundary
            dfs(0, j)
        if grid[m - 1][j] == 1:  # Bottom boundary
            dfs(m - 1, j)
    
    # Count the remaining land cells that are not connected to the boundary
    count = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1:
                count += 1
    
    return count
