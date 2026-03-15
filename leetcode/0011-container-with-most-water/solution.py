class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
         0  1  2  3  4  5  6  7  8     
        [1, 8, 6, 2, 5, 4, 7, 3, 2]
         ^  1  2  3  4  5  6  7  8
            ^  6  4 15 16 35 18 14
               ^  2 10 12 24 15 12
                  ^  2  4  6  8 10
                     ^  4 10  9  8
                        ^ 
        
        h[l] < h[r]
        W
        Area0 = W * min(h[l], h[r])

        if move r to r - 1
        Area1 = (W - 1) * min(h[l], h[r - 1])

        because h[r] > h[l], so min(h[l], h[r]) = h[l]
        h[l] <= min(h[l], h[r - 1])
        W < W - 1

        which means: Area1 < Area0

        Conclusion: when h[l] < h[r], move r inwards will always shrink the area
        """
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            best = max(best, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best
