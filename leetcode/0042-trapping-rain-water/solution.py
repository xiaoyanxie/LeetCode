class Solution:
    def trap(self, height: List[int]) -> int:
        #two pointer
        if len(height) == 1 or len(height) == 2:
            return 0
        res = 0
        l = 0
        r = len(height) - 1
       
        lmax = l
        rmax = r
        res = 0
        while l < r:
            if height[l] < height[lmax]:
                res += height[lmax] - height[l]
            else:
                lmax = l
            if height[r] < height[rmax]:
                res += height[rmax] - height[r]
            else:
                rmax = r
            if height[lmax] > height[rmax]:
                r -= 1
            else:
                l += 1
        
        return res
    


    #compare pointers and move the shorter one
    #check the current ele with lmax/rmax, if bigger, replace old ones, if smaller, get diff and put in res

