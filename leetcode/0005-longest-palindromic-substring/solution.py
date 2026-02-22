class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j) -> str:
            if s[j] != s[i]:
                return ''
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1: j]

        best = ''
        for i in range(len(s)):
            s1 = expand(i, i)
            if len(s1) > len(best):
                best = s1
            if i > 0:
                s2 = expand(i - 1, i)
                if len(s2) > len(best):
                    best = s2
        return best
