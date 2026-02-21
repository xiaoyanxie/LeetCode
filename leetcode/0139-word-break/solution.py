class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:        
        wordSet = set(wordDict)
    

        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)+1):
            for j in range(0, i+1):
                if dp[j] == True:
                    if s[j:i] in wordSet:
                        dp[i] = True
                        break
        
        return dp[len(s)]
      
