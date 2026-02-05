class Solution:
    def climbStairs(self, n: int) -> int:

        # @cache
        # def dfs(remain):
        #     if remain == 0:
        #         return 1
        #     if remain >= 2:
        #         return dfs(remain-2) + dfs(remain-1)
        #     return dfs(remain-1)
            
        # return dfs(n)

        #subproblem: how many kinds of ways i have to reach cur place dp[i] = dp[i-1] + dp[i-2]
        #base case: dp[0] = 0, dp[1] = 1

        #n = 2
        mem = [0] * (n + 1) #[1,1,0,0]
        mem[0] = 1
        mem[1] = 1

        for i in range(2,n+1):
            mem[i] = mem[i-1] + mem[i-2]

        return mem[n]

