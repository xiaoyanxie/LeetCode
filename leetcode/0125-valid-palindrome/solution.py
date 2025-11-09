class Solution:
    def isPalindrome(self, s: str) -> bool:
        # initialize two pointers
        i = 0
        j = len(s) - 1
        #iterate over the whole string to compare 
        #abbbba
        # ^  ^
        #->   <-
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True



# The two-pointer algorithm runs in O(n) time because each character in the string is checked at most once by one of the pointers. It uses only O(1) extra space since it only needs to keep track of two indices (the left and right pointers).




