class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j, i0, j0):
            if grid[i][j] == 0:
                return
            
            grid[i][j] = 0
            self.coor.append((i-i0, j-j0))
            for dx, dy in [(1, 0),(-1, 0),(0,1),(0,-1)]:
                nx, ny = i +dx, j + dy
                if 0<=nx<len(grid) and 0 <= ny <len(grid[0]):
                    
                    dfs(grid, nx, ny, i0, j0)
            return

        count = 0
        islands = set()
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                
                if grid[i][j] == 0:
                    continue
                self.coor = list()
                dfs(grid, i, j, i, j)
                self.coor.sort()
                islands.add(tuple(self.coor))
                    
        return len(islands)
                
        
        

