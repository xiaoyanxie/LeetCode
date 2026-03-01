class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        30,11,23,4,20

        4,11,20,23,60   h = 7
        
        sum([ math.ceil(pile / x) for pile in piles ]) <= h

        p1.  p2       pn
        -- + -- + ... --  <= h
        x     x        x
        """
        
        minK, maxK = 1, max(piles)
        found = -1
        while minK <= maxK:
            midK = minK + (maxK - minK) // 2
            if sum([ math.ceil(pile / midK) for pile in piles ]) <= h:
                found = midK
                maxK = midK - 1
            else:
                minK = midK + 1
        # print(found)
        return found
