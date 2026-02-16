from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        freq = defaultdict(int)
        maxlen = 0
        for r, c in enumerate(s):

            freq[c] += 1

            while freq[c] > 1:
                freq[s[l]] -= 1
                l += 1

            maxlen = max(maxlen, r - l + 1)
        
        return maxlen

