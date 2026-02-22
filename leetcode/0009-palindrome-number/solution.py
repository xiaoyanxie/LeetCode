class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        a = 0
        b = 121
        """
        a, b = x, 0
        while a > 0:
            b *= 10
            b += a % 10
            a //= 10
        return x == b
