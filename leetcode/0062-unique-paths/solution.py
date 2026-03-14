class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #subproblem: for the dp[i], robot can come from two dirctions, 
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        for i in range(1, m):
            dp[i][0] = dp[i - 1][0]
        for j in range(1, n):
            dp[0][j] = dp[0][j - 1]
            
        for i in range(1, m):
            for j in range(1, n):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i][j - 1] + dp[i - 1][j]
        
        return dp[m - 1][n - 1]
