class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0
        m = len(grid)
        n = len(grid[0])
        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

        def isValidLoc(i, j) -> bool:
            return 0 <= i < m and 0 <= j < n

        """
        visited: (0, 0), (0, 1), (1, 0), (1, 1), (2, 0), (2, 1), (0, 2), (0, 3), (1, 3)

            0   1   2   3   4
        0 ["1","1","1","1","0"],
        1 ["1","1","0","1","0"],
        2 ["1","1","0","0","0"],
        3 ["0","0","0","0","0"]
        
        """

        def visit(i, j):
            visited.add((i, j))
            stack = [(i, j)] # (1, 3)
            while stack:
                i, j = stack.pop()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if not isValidLoc(ni, nj) or grid[ni][nj] == '0' or (ni, nj) in visited:
                        continue
                    stack.append((ni, nj))
                    visited.add(stack[-1])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in visited:
                    visit(i, j)
                    islands += 1
        
        return islands

