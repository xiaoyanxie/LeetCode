class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # s = "abcabcbb"
        #             ^

        l = 0 # 7
        seen = {} # {a: 3, b: 7, c: 5}
        maxLen = 0 # 1
        for r in range(len(s)): # r = 7
            if s[r] in seen and seen[s[r]] >= l:
                l = seen[s[r]] + 1
            
            seen[s[r]] = r

            newLen = r - l + 1
            if newLen > maxLen:
                maxLen = newLen

        return maxLen
