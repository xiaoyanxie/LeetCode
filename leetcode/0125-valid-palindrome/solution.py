class Solution:
    def isPalindrome(self, s: str) -> bool:
        #clean the given string
        s_lower = s.lower()
        s_clean = [char for char in s_lower if char.isalnum()]

        #reverse string check
        return s_clean == s_clean[::-1]

        # left = 0
        # right = len(s) - 1
        # while left < right:
        #     if not s[left].isalnum():
        #         left += 1
        #         continue
        #     elif not s[right].isalnum():
        #         right -= 1
        #         continue
        #     elif s[left].lower() == s[right].lower():
        #         left += 1
        #         right -= 1
        #     else:
        #         return False
        
        # return True
