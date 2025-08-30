class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #prices = [7,1,5,3,6,4]
        #          ^ 
        profit = 0
        maxP = 0
        min = float('inf')
        for p in prices:
            if p < min:
                min = p
            else:
                profit = p - min
                maxP = max(maxP, profit)
        
        return maxP


