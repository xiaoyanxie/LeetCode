class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        abbca
         l
          r
        """

        def checkPalindrome(l, r) -> Tuple[int, int]:
            while l < r and s[l] == s[r]:
                l += 1
                r -= 1
            return l, r

        l0, r0 = checkPalindrome(0, len(s) - 1)
        if l0 >= r0:
            return True
        
        # deleting one char on the left
        l1, r1 = checkPalindrome(l0 + 1, r0)
        if l1 >= r1:
            return True
        
        # deleting one char on the right
        l2, r2 = checkPalindrome(l0, r0 - 1)
        return l2 >= r2
