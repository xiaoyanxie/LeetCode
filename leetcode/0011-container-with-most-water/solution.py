class Solution:
    #[8,7,2,1]
    # ^     ^1*3=3
    #l,i r,j
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        
        i = 0 
        j = len(height) - 1

        max = (r-l) * min(height[l], height[r])
        while i < j:
            square = (j - i) * min(height[j], height[i])
            if square <= max:
                if height[i] > height[j]:
                    j -= 1
                else:
                    i += 1
            if square > max:
                max = square
                l = i
                r = j

        return max
        #square:
        #1. square less than or equal to: move the shorter edge
        #2. bigger than : store left and right pointer and max
