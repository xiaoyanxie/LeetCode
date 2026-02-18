from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        [2,1,1],
        [1,1,0],
        [0,1,1]

        [2,1,1],
        [1,1,1],
        [0,1,2]

        [2,2],
        [1,1],
        [0,0],
        [2,0]

        Use BFS, return max height
        """
        rows = len(grid)
        cols = len(grid[0])
        visited = set()

        def isValidLoc(i, j):
            return 0 <= i < rows and 0 <= j < cols

        fresh = 0
        queue = deque()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] in (1, 2):
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append( (i, j, 0) )
                    visited.add((i, j))

        maxtime = 0
        while queue:
            i, j, time = queue.popleft()
            maxtime = max(time, maxtime)
            for di, dj in [ (0, 1), (0, -1), (1, 0), (-1, 0) ]:
                ni, nj = i + di, j + dj
                if not isValidLoc(ni, nj) or (ni, nj) in visited or grid[ni][nj] != 1:
                    continue
                queue.append((ni, nj, time + 1))
                visited.add((ni, nj))
        
        if fresh != len(visited):
            return -1
        
        return maxtime
