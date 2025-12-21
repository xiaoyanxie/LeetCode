class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(string, i, j):
            while i < j:
                if string[i] != string[j]:
                    return False
                i +=1
                j-=1
            return True


        left = 0 
        right = len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -=1
            else:
                return isPalindrome(s, left+1, right) or isPalindrome(s, left, right-1)

        return True
            
        
