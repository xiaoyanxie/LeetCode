class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        def dfs(grid, i, j):
            if grid[i][j] == 1:
                return
            grid[i][j] = 1
            if i > 0:
                dfs(grid, i-1,j)
            if j > 0:
                dfs(grid, i, j-1)
            if i < len(grid) - 1:
                dfs(grid, i+1, j)
            if j < len(grid[0]) - 1:
                dfs(grid, i, j + 1)    
            return
        
        # def findIsland(gird, i, j):
        #     if grid[i][j] == 1:
        #         return
        #     if grid[i][j] == 0:
        #         grid[i][j] == 1
            
        #     if i > 0:
        #         dfs(grid, i-1,j)
        #     if j > 0:
        #         dfs(grid, i, j-1)
        #     if i < len(grid) - 1:
        #         dfs(grid, i+1, j)
        #     if j < len(grid[0]) - 1:
        #         dfs(grid, i, j + 1)    
        #     return
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 or j == 0 or i == len(grid) - 1 or j == len(grid[0]) - 1:
                    dfs(grid, i, j)
        
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    continue
                dfs(grid, i, j)
                count += 1
        return count

        
