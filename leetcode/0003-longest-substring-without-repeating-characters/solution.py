class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        best = 3
        window: {b,c,a}
        abcabcbb
         l
           r
        """

        window = [0] * 256
        best = 0
        l = 0
        for r, c in enumerate(s):
            while window[ord(c)] == 1:
                window[ord(s[l])] = 0
                l += 1
            window[ord(c)] = 1
            best = max(best, r - l + 1)

        return best
