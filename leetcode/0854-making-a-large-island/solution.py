from collections import defaultdict
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

        islandId = 2
        areas = defaultdict(int)
        
        def isValidLoc(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def visitIslands(i, j):
            stack = [(i, j)]
            grid[i][j] = islandId
            area = 0
            while stack:
                i, j = stack.pop()
                area += 1
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if not isValidLoc(ni, nj) or grid[ni][nj] != 1:
                        continue
                    stack.append((ni, nj))
                    grid[ni][nj] = islandId
            return area
                    
        maxArea = 1

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    area = visitIslands(i, j)
                    areas[islandId] = area
                    maxArea = max(maxArea, area)
                    islandId += 1
        
        # print(grid)
        # print(areas)
        
        def visitSea(i, j):
            stack = [(i, j)]
            largest = 0
            while stack:
                i, j = stack.pop()
                grid[i][j] = -1

                adjAreas = defaultdict(int)
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if not isValidLoc(ni, nj):
                        continue

                    if grid[ni][nj] in areas:
                        adjAreas[grid[ni][nj]] = areas[grid[ni][nj]]

                    if grid[ni][nj] == 0:
                        stack.append((ni, nj))
                
                largest = max(largest, sum(adjAreas.values()) + 1)
            
            return largest

        # print(maxArea)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    maxAdjArea = visitSea(i, j)
                    maxArea = max(maxArea, maxAdjArea)
        return maxArea
