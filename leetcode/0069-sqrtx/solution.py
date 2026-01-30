class Solution:
    def mySqrt(self, x: int) -> int:
        # search within [0, x]
        l = 0
        r = x
        while l <= r:
            mid = l + (r - l) // 2
            sqr = mid * mid
            if sqr == x:
                return mid
            if sqr < x < (mid + 1) * (mid + 1):
                return mid
            if x < sqr:
                r = mid - 1
            elif x > sqr:
                l = mid + 1
        return 0
