class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                nx, ny = i + dx, j + dy
                if 0<= nx < len(grid) and 0 <= ny < len(grid[0]):
                    dfs(grid, nx, ny)
            
            return
        
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "0":
                    continue
                dfs(grid, i, j)
                count += 1
        
                
        
        return count
        
