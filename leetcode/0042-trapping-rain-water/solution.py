class Solution:
    def trap(self, height: List[int]) -> int:
        """
  total: 6
   lmax: 3
 rmaxes: 3  3  3  3  3  3  3  2  2  2  1  0
        [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
                                          r
        """

        lmax = 0
        rmaxes = [0] * len(height)
        for i in reversed(range(1, len(height))):
            if height[i] > rmaxes[i]:
                rmaxes[i - 1] = height[i]
            else:
                rmaxes[i - 1] = rmaxes[i]
        
        total = 0
        for i, h in enumerate(height):
            diff = min(lmax, rmaxes[i]) - h
            if diff > 0:
                total += diff
            
            if h > lmax:
                lmax = h
        
        return total
