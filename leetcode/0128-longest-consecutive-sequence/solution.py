class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unseen = set(nums)

        def visit(n):
            length = 0
            k = n
            while k in unseen:
                length += 1
                unseen.remove(k)
                k += 1
                
            l = n - 1
            while l in unseen:
                length += 1
                unseen.remove(l)
                l -= 1
                
            return length

        best = 0
        for n in nums:
            if n in unseen:
                length = visit(n)
                best = max(best, length)
        return best
