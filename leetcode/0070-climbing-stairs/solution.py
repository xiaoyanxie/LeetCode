class Solution:
    def climbStairs(self, n: int) -> int:

        @cache
        def climb(steps):
            if steps == n:
                return 1
            
            ways = 0
            if steps + 1 <= n:
                ways += climb(steps + 1)
            if steps + 2 <= n:
                ways += climb(steps + 2)
            return ways
        
        return climb(0)
