def numIslands(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    num_islands = 0
    
    def dfs(r, c):
        if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
            return
        grid[r][c] = '0'  # Mark the cell as visited by setting it to '0'
        # Explore all 4 directions
        dfs(r - 1, c)  # Up
        dfs(r + 1, c)  # Down
        dfs(r, c - 1)  # Left
        dfs(r, c + 1)  # Right
    
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':  # Found an unvisited island
                num_islands += 1
                dfs(i, j)  # Mark the entire island
    
    return num_islands
