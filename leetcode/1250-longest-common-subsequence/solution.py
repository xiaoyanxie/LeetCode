class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [ [0] * (len(text2) + 1) for _ in range(len(text1) + 1) ]

        for i, t1 in enumerate(text1):
            for j, t2 in enumerate(text2):
                k, l = i + 1, j + 1
                if t1 == t2:
                    dp[k][l] = dp[k - 1][l - 1] + 1
                else:
                    dp[k][l] = max(dp[k - 1][l], dp[k][l - 1])
        
        return dp[-1][-1]
