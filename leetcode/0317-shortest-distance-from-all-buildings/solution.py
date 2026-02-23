from collections import deque, defaultdict
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]


        """
           0 1 2 3 4
        0 [1,0,2,0,1],
        1 [0,0,0,0,0],
        2 [0,0,1,0,0]
        """
        
        def isValidLoc(i, j):
            return 0 <= i < rows and 0 <= j < cols

        land2Building = {}

        def bfs(starti, startj):
            queue = deque([(starti, startj, 0)])
            visited = set([(starti, startj)])
            while queue:
                i, j, steps = queue.popleft()
                # if grid[i][j] == 1:
                #     # print(f'steps from ({starti},{startj}) to ({i},{j}) = {steps}')
                #     totalSteps += steps
                #     buildings += 1
                #     if buildings == totalBuildings:
                #         break
                #     continue
                if grid[i][j] == 0:
                    # print(f'steps from ({starti},{startj}) to ({i},{j}) = {steps}')
                    if (i, j) not in land2Building:
                        land2Building[(i, j)] = [steps, 1]
                    else:
                        land2Building[(i, j)][0] += steps
                        land2Building[(i, j)][1] += 1

                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if not isValidLoc(ni, nj) or grid[ni][nj] != 0 or (ni, nj) in visited:
                        continue
                    visited.add((ni, nj))
                    queue.append((ni, nj, steps + 1))
            # print(f'({starti}, {startj}) buildings={buildings}, totalBuildings={totalBuildings}, distance={totalSteps}')
            # return totalSteps
        
        totalBuildings = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] != 1: continue
                totalBuildings += 1
                bfs(i, j)
        
        best = inf
        for k in land2Building:
            dist, num = land2Building[k]
            if num != totalBuildings: continue
            best = min(best, dist)

        return best if best != inf else -1
