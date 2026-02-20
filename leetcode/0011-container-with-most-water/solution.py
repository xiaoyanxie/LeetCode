class Solution:
    def maxArea(self, height: List[int]) -> int:
        #amount of water = (j - i) * min(height[i], height[j])
        l = 0
        r = len(height) - 1
        maxAmount = 0
        while l < r:
            amount = (r - l) * min(height[l], height[r])
            if amount > maxAmount: 
                maxAmount = amount
            if height[l]> height[r]:
                r -= 1
            else:
                l += 1
        return maxAmount
        
