class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        buy = 1
        profit = 5
        7,1,5,3,6,4
        7 1 1 1 1 1
        """
        buy = prices[0]
        maxProfit = 0
        for p in prices:
            if p < buy:
                buy = p
            else:
                maxProfit = max(p - buy, maxProfit)
        return maxProfit
