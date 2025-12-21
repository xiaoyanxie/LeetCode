class Solution:
    def makePalindrome(self, s: str) -> bool:
        count = 0
        l = 0 
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                count +=1
            l += 1
            r -= 1
            if count > 2:
                return False
        return True   

