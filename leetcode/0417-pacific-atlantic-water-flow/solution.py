class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificFlowables = set()
        atlanticFlowables = set()
        rows = len(heights)
        cols = len(heights[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def isValidLoc(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def climbUpHill(i, j, flowables):
            flowables.add((i, j))
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if not isValidLoc(ni, nj) or (ni, nj) in flowables:
                    continue
                if heights[i][j] <= heights[ni][nj]:
                    climbUpHill(ni, nj, flowables)

        #pacific beach
        for i in range(rows):
            j = 0
            climbUpHill(i, j, pacificFlowables)

        for j in range(cols):
            i = 0
            climbUpHill(i, j, pacificFlowables)

        #atlantic beach
        for i in range(rows):
            j = cols - 1
            climbUpHill(i, j, atlanticFlowables)

        for j in range(cols):
            i = rows - 1
            climbUpHill(i, j, atlanticFlowables)

        return list(pacificFlowables & atlanticFlowables)
