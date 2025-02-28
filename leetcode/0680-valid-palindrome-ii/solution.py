class Solution:
    def validPalindrome(self, s: str) -> bool:
        # def isPalindrome(i,j):
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True

        left = 0
        right = len(s) - 1
        # while left < right:
        #     if s[left] != s[right]:
        #         return isPalindrome(left + 1, right) or     isPalindrome(left, right - 1)
        #     left += 1
        #     right -= 1
            
        # return True
        while left < right and s[left] == s[right]:
            left += 1
            right -= 1
        return (s[left:right] == s[left:right][::-1]) or (s[left+1:right+1] == s[left+1:right+1][::-1])
