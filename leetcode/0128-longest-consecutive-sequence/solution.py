class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        100,4,200,1,3,2

        100 +1 -1
        4 +1
        4 -1(3) -2(2) -3(1) -4
        200 +1 -1
        """

        unexplored = set(nums)
        best = 0

        def explore(n):
            cnt = 0
            # left
            left = n
            while left in unexplored:
                unexplored.remove(left)
                cnt += 1
                left -= 1
            
            # right
            right = n + 1
            while right in unexplored:
                unexplored.remove(right)
                cnt += 1
                right += 1
        
            return cnt
        
        for n in nums:
            if n in unexplored:
                length = explore(n)
                best = max(best, length)
        assert not unexplored
        return best
