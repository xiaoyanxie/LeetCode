from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = defaultdict(int)
        maxLen = 0
        l = 0
        for r, c in enumerate(s):
            freq[c] += 1
            while r - l + 1 - max(freq.values()) > k:
                freq[s[l]] -= 1
                l += 1

            maxLen = max(maxLen, r - l + 1)
        return maxLen
