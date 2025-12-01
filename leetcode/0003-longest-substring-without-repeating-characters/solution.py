class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}

        l = 0
        maxLen = 0

        for r, c in enumerate(s):
            if c in seen and seen[c] >= l:
                l = seen[c] + 1
            seen[c] = r
            maxLen = max(maxLen, r - l + 1)

        return maxLen

