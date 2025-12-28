# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left = 1
        right = n
        #mid = 1 
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid - 1) or mid == 1:
                    return mid
                right = mid
            else:
                left = mid + 1
        return left + (right - left) // 2
            
        
