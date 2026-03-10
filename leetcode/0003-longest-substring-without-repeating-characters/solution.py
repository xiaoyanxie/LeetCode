class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        best = 3
        seen: {}
        abcabcbb
               i
               j
        """

        best = 0
        seen = set()
        i = 0
        for j, c in enumerate(s):
            while c in seen:
                seen.remove(s[i])
                i += 1
            
            seen.add(c)
            best = max(best, j - i + 1)

        return best
