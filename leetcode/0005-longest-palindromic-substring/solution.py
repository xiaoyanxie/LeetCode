class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i,j):
            l = float('inf')
            r = -float('inf')
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    l = i
                    r = j
                    i -= 1
                    j += 1
                    continue
                else:
                    break
                
            if r - l + 1 > self.maxLen:
                self.start = l
                self.maxLen = r - l + 1
            return
        
        if len(s) <= 1:
            return s
        self.start = 0
        self.maxLen = 1
        for i in range(1, len(s)):
            expand(i,i)
            expand(i-1, i)
            
        return s[self.start: self.start + self.maxLen]




