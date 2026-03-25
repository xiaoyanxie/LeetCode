class Solution:
    def trap(self, height: List[int]) -> int:
        """
        trapped = 0
        l, r = 0, len(height)
        loop:
            if lmax <= rmax:
                # move l
                trapped += lmax - height[l]
                # calculate lmax
            else:
                # move r
                trapped += rmax - height[r]
                # calculate rmax
        
        lmax = 3
        rmax = 2
        total: 6
        0,1,0,2,1,0,1,3,2,1,2,1
                      l
                      r
        """
        l, r = 0, len(height) - 1
        lmax, rmax = height[l], height[r]
        total = 0

        while l < r:
            if lmax <= rmax:
                l += 1
                if lmax >= height[l]:
                    total += lmax - height[l]
                else:
                    lmax = height[l]
            else:
                r -= 1
                if rmax >= height[r]:
                    total += rmax - height[r] 
                else:
                    rmax = height[r]
        
        return total
