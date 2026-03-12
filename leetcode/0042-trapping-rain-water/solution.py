class Solution:
    def trap(self, height: List[int]) -> int:
        """
  total:16
   lmax:7
   rmax:7

        5,5,1,7,1,1,5,2,7,6
                  l
                      r

        4,2,0,3,2,5
          l
                  r

        0,1,0,2,1,0,1,3,2,1,2,1
                    l
                          r
        """
        l, r = 0, len(height) - 1
        lmax = height[l]
        rmax = height[r]
        total = 0

        def collect(h):
            delta = min(rmax, lmax) - h
            return delta if delta > 0 else 0

        while l <= r:
            if lmax <= rmax:
                total += collect(height[l])
                # print(f'{lmax} <= {rmax} collect {collect(height[l])} at {l}')
                lmax = max(lmax, height[l])
                l += 1
            else:
                total += collect(height[r])
                # print(f'{lmax} > {rmax} collect {collect(height[r])} at {r}')
                rmax = max(rmax, height[r])
                r -= 1
        
        return total
