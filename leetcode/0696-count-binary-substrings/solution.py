class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        """
 prev   00222222
 curr.  12121212
        00110011
        
        total: 6

 prev   011
 curr   112
        011

        total: 1
        """
        prev = 0
        curr = 1
        total = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]: # same group
                curr += 1
            else: # different group
                prev = curr
                curr = 1

            if prev >= curr:
                total += 1
        
        return total
