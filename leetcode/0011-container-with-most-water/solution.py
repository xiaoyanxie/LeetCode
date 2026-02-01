class Solution:
    def maxArea(self, height: List[int]) -> int:
        # [1,8,6,2,5,4,8,3,7]
        #  0 - 8, len = 8, area = 8
        #  1 - 8, len = 7, area = 49
        #  1 - 7, len = 6, area = 18
        #  2 - 8, len = 6, area = 36
        #  2 - 7, len = 5, area = 15

        # [1,2,4,3]
        #  0 - 3, area = 3
        #  
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            area = (r - l) * min(height[r], height[l])
            # print(f"l = {l}, r = {r}, area = {area}")
            if area > maxArea:
                maxArea = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxArea
