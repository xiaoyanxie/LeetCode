class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # m = len(grid)
        # n = len(grid[0])
        # minSum = [[0] * n for _ in range(m)]
        # for i in range(m):
        #     for j in range(n):
        #         if i == 0 and j == 0:
        #             minSum[i][j] = grid[i][j]
        #         elif i == 0 and j != 0:
        #             minSum[i][j] = grid[i][j] + minSum[i][j-1]
        #         elif i != 0 and j == 0:
        #             minSum[i][j] = grid[i][j] + minSum[i-1][j]
        #         else:
        #             minSum[i][j] = grid[i][j] + min(minSum[i][j-1], minSum[i-1][j])
        
        # return minSum[m-1][n-1]

        #subproblem: minSum from (0,0) to current grid: minSum[i][j] = grid[i][j] + min(minSum[i][j-1], minSum[i-1][j])) #subproblems: mn 
        #rumtime and extra space O(mn)

        @cache
        def dp(i,j):
            if i == 0 and j == 0:
                return grid[i][j]
            # if minSum[i][j] != 0:
            #     return minSum[i][j]
            if i == 0:
                return grid[i][j] + dp(i, j-1)
            elif j == 0:
                return grid[i][j] + dp(i-1, j)
            # else:
            return grid[i][j] + min(dp(i,j-1),dp(i-1,j))
            # return minSum[m-1][n-1]
        m = len(grid)
        n = len(grid[0])
        # i,j=x,0
        # minSum = [[0]*n for _ in range(m)]
        return dp(m-1, n-1)
        # return minSum[m-1][n-1]
