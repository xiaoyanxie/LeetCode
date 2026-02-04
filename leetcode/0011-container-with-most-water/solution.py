class Solution:
    def maxArea(self, height: List[int]) -> int:

        # [1,1,1,10,10,2,2,2]
        #        l         r

        l, r = 0, len(height) - 1
        maxArea = 0
        while l < r:
            hl, hr = height[l], height[r]
            area = min(hl, hr) * (r - l)
            if area > maxArea:
                maxArea = area
            if hl > hr:
                r -= 1
            else:
                l += 1

        return maxArea
