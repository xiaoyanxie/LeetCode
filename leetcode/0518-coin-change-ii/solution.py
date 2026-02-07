class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
    
        if amount == 0:
            return 1
        dp = [0] * (amount + 1)
        for c in coins:
            for i in range(1, amount + 1):
                if i - c > 0:
                    dp[i] += dp[i-c]
                if i - c == 0:
                    dp[i] += 1
            
        if not dp[amount]:
            return 0
        return dp[amount]
        

    
