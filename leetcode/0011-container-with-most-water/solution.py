class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        best = 0
        while l < r:
            w = r - l
            h = min(height[l], height[r])
            best = max(w * h, best)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return best
