class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        abbc
           ^
            ^
        a,b,bb,b,c
        cbaabc
             ^
         ^
        count = 1
        for i in range(1, len(s)):
            expand(i,i)
            expand(i -1,i)
        def expand(i,j):
            counter = 0
            self.count += 1
        """
        def expand(i,j):
            count = 0
            while i >= 0 and j < len(s):
                if s[i] == s[j]:
                    count += 1
                else:
                    return count
                i -= 1
                j += 1
            return count
        
        if len(s) <= 1:
            return 1
        res = 1
        for i in range(1, len(s)):
            m = expand(i-1, i)
            n = expand(i, i)
            res = res + m + n
        return res
       
