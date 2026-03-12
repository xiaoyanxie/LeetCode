class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        babad

        cbbd
        """

        def expand(i, j) -> str:
            """
            aabaa
            i
                 j
            
            cbbd
             i
               j

            a
            i
             j
            """
            while 0 <= i and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return s[i + 1:j]
        
        best = s[0]
        for i in range(len(s)):
            p1 = expand(i, i)
            if len(p1) > len(best):
                best = p1

            p2 = expand(i, i + 1)
            if len(p2) > len(best):
                best = p2
        return best
