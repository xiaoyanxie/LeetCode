from collections import defaultdict

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def isValidCoordinate(i, j):
            return 0 <= i < len(heights) and 0 <= j < len(heights[0])

        pacificFlowables = set()
        atlanticFlowables = set()
        def traceUpHill(i, j, flowables, visited):
            visited.add((i, j))
            flowables.add((i, j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if not isValidCoordinate(ni, nj) or (ni, nj) in visited:
                    continue
                # visited.add((ni, nj))
                if heights[i][j] <= heights[ni][nj]:
                    traceUpHill(ni, nj, flowables, visited)

        for j in range(len(heights[0])):
            i = 0
            visited = set()
            visited.add((i, j))
            pacificFlowables.add((i, j))
            traceUpHill(i, j, pacificFlowables, visited)
        for i in range(len(heights)):
            j = 0
            visited = set()
            visited.add((i, j))
            pacificFlowables.add((i, j))
            traceUpHill(i, j, pacificFlowables, visited)
        
        for j in range(len(heights[0])):
            i = len(heights) - 1
            visited = set()
            visited.add((i, j))
            atlanticFlowables.add((i, j))
            traceUpHill(i, j, atlanticFlowables, visited)
        for i in range(len(heights)):
            j = len(heights[0]) - 1
            visited = set()
            visited.add((i, j))
            atlanticFlowables.add((i, j))
            traceUpHill(i, j, atlanticFlowables, visited)
        # print(pacificFlowables)
        # print(atlanticFlowables)
        return list(pacificFlowables & atlanticFlowables)
