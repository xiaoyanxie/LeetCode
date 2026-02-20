from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        seen = set()
        l = 0
        r = 0
        maxCount = 0

        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r += 1
            else:
                maxCount = max(r-l, maxCount)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(s[r])
                r += 1
                
        return max(maxCount, r-l)
