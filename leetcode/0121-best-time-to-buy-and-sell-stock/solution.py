class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > min:
                maxProfit = max(prices[i] - min, maxProfit)
            else:
                min = prices[i]
        return maxProfit
