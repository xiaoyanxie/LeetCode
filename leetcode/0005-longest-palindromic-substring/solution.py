class Solution:
    def longestPalindrome(self, s: str) -> str:
        def buildPalindrome(l: int, r: int):
            while 0 <= l and r < len(s) and s[l] == s[r]:
                l = l - 1
                r = r + 1
            return l + 1, r - 1
        
        start, maxLen = 0, 0
        for i in range(0, len(s)):
            l1, r1 = buildPalindrome(i, i)
            p1 = r1 - l1 + 1
            if p1 > maxLen:
                maxLen = p1
                start = l1
            
            l2, r2 = buildPalindrome(i, i + 1)
            p2 = r2 - l2 + 1
            if p2 > maxLen:
                maxLen = p2 
                start = l2
        
        return s[start: start + maxLen]
