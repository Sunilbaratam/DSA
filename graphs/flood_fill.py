def flood_fill(image, sr, sc, newcolor):
    if image[sr][sc]==newcolor:
        return image
    
    def dfs(r,c):
        if (r<0 or r>len(image) or c<0 or c>len(image[0]) or image[r][c]!=newcolor):
            return 
        
        image[r][c]=newcolor
        dfs(r-1,c)
        dfs(r+1,c)
        dfs(r,c-1)
        dfs(r,c+1)

    dfs(sr,sc)
    return image
