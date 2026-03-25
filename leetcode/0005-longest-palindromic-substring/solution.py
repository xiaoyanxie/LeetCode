class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(i, j) -> tuple[int, int]:
            # expand and return the length
            """
            abccbd
            i
                 j         

            abcbd
            i
             j    
            """
            while 0 <= i and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            # print(f'{s[i + 1:j]}')
            return i + 1, j
        
        best = [0, 1]
        for i in range(len(s)):
            l, r = expand(i, i)
            if r - l > best[1] - best[0]:
                best[0] = l
                best[1] = r
            if i + 1 == len(s):
                break
            
            l, r = expand(i, i + 1)
            if r - l > best[1] - best[0]:
                best[0] = l
                best[1] = r
        return s[best[0]: best[1]]
            
