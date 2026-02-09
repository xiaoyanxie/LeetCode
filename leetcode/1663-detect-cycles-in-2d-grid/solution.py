class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        direction = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        def dfs(i,j,px,py):
            visited[i][j] = True

            for x,y in direction:
                nx,ny = x + i,y+j
                if (nx,ny) == (px,py):
                    continue
                if 0<= nx < m and 0 <= ny < n and grid[i][j] == grid[nx][ny]:
                    if visited[nx][ny]:
                        return True
                    
                    if dfs(nx, ny, i, j):
                        return True
            return False
        
        for i in range(m):
            for j in range(n):
                if not visited[i][j]:
                    if dfs(i,j,-1,-1):
                        return True
        
        return False
