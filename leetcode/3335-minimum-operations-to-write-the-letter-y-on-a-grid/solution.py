class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        """
        freq: {0:3, 1:1, 2:1}
        freqY:{0:0, 1:3, 2:1}

        [[1,2,2],
         [1,1,0],
         [0,1,0]]
        
        """

        freq  = {0:0, 1:0, 2:0}
        freqY = {0:0, 1:0, 2:0}

        n = len(grid)
        center = (n // 2, n // 2) # (1, 1)
        def isOnYShape(i, j):
            if (i == j or i == n - j - 1) and i < center[0]:
                return True
            if j == n // 2 and i >= center[1]:
                return True
            return False

        for i in range(n):
            for j in range(n):
                if isOnYShape(i, j):
                    freqY[grid[i][j]] += 1
                else:
                    freq[grid[i][j]] += 1
        
        """
        freq: {0:3, 1:1, 2:1}
        freqY:{0:0, 1:3, 2:1}

        """
        best = inf # 3
        for valueY in freqY:
            changeInY = sum( freqY[k] for k in freqY if k != valueY ) # 1
            for value in freq:
                if value != valueY:
                    changeInBoard = sum( freq[k] for k in freq if k != value ) # 2
                    best = min(best, changeInY + changeInBoard)
        return best
