from collections import deque, defaultdict
class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        houses = [ (i, j) for i in range(m) for j in range(n) if grid[i][j] == 1 ]

        def isValidLoc(i, j) -> bool:
            return 0 <= i < m and 0 <= j < n

        landToHouse = defaultdict(lambda: [0, 0]) # [dist, houses]
        best = inf
        excluded = set()
        def bfsToLands(i0, j0, reachCnt):
            nonlocal best
            visited = set()
            queue = deque([(i0, j0, 0)])
            visited.add((i0, j0))
            while queue:
                i, j, d = queue.popleft()
                if grid[i][j] == 0:
                    landToHouse[(i, j)][0] += d
                    landToHouse[(i, j)][1] += 1
                    if landToHouse[(i, j)][1] == len(houses):
                        best = min(best, landToHouse[(i, j)][0])
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if not isValidLoc(ni, nj) or grid[ni][nj] != 0 or (ni, nj) in visited:
                        continue
                    if (ni, nj) in excluded:
                        continue
                    if landToHouse[(ni, nj)][1] != reachCnt:
                        excluded.add((ni, nj))
                        continue
                    queue.append((ni, nj, d + 1))
                    visited.add((ni, nj))

        for k, (i, j) in enumerate(houses):
            bfsToLands(i, j, k)
        return best if best != inf else -1
