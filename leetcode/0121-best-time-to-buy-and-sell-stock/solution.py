class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        best = 0
        
        for sell, sellPrice in enumerate(prices):
            gain = sellPrice - prices[buy]
            if gain < 0:
                buy = sell
                continue
            best = max(best, gain)

        return best
