class Solution:
    def isPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        def isEnglish(c):
            return ord('a') <= ord(c) <= ord('z') or ord('A') <= ord(c) <= ord('Z')

        def isNumber(c):
            return ord('0') <= ord(c) <= ord('9')

        while i <= j:
            if not isEnglish(s[i]) and not isNumber(s[i]):
                i += 1
                continue
            if not isEnglish(s[j]) and not isNumber(s[j]):
                j -= 1
                continue
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True
