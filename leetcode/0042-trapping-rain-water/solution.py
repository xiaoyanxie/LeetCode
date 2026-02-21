class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]

        """
        total   : 6
        leftMax : 3
        rightMax: 2
        [0,1,0,2,1,0,1,3,2,1,2,1]
         l                     
                               r
        """
        
        total = 0
        while l < r:
            if leftMax <= rightMax:
                acc = leftMax - height[l]
                l += 1
                if acc > 0:
                    total += acc
                leftMax = max(leftMax, height[l])
            else:
                acc = rightMax - height[r]
                r -= 1
                if acc > 0:
                    total += acc
                rightMax = max(rightMax, height[r])
        return total
