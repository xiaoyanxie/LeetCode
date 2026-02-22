class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]
        # visited = set()

        def isValidLoc(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def visit(i, j):
            stack = [(i, j)]
            while stack:
                i, j = stack.pop()
                # visited.add((i, j))
                grid[i][j] = '2'
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if not isValidLoc(ni, nj) or grid[ni][nj] != '1': # or (ni, nj) in visited:
                        continue
                    stack.append((ni, nj))
        
        islands = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != '1': # or (i, j) in visited:
                    continue
                islands += 1
                visit(i, j)
        return islands
