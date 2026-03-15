class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        count = 0

        def dfs(i,j):
            if grid[i][j] == "0":
                return
            grid[i][j] = "0"
            
            dire = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for a, b in dire:
                nx, ny = i + a, j + b
                if 0 <= nx < m and 0 <= ny < n:
                    dfs(nx, ny)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        return count
