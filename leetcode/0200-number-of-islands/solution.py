class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Time: O(M * N)
        # Space: O(1)
    
        # visited = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)] 
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i, j):
            stack = [(i, j)]
            grid[i][j] = '0'
            while stack:
                i, j = stack.pop()
                # neighbors
                for d in directions:
                    k, l = i + d[0], j + d[1]
                    if 0 <= k < rows and 0 <= l < cols and grid[k][l] == '1':
                        stack.append((k, l))
                        grid[k][l] = '0'

        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    islands += 1

        return islands
