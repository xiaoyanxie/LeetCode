class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        profit: 5
        buy = 1
        7,1,5,3,6,4
                   i
        """
        profit = 0
        buy = 10**5
        for price in prices:
            profit = max(profit, price - buy)
            buy = min(buy, price)
        return profit
