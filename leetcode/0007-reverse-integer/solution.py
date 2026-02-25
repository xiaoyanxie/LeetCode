class Solution:
    MIN, MAX = -0x8000_0000, 0x7FFF_FFFF

    def reverse(self, x: int) -> int:
        negative = x < 0

        """
        MIN <= -ret * 10 - x % 10 
        is identical to:
        - (MIN + x % 10) / 10 >= ret

        ret * 10 + x % 10 <= MAX
        is identical to:
        ret <= (MAX - x % 10) / 10
        """
        def check(num, digit):
            if negative and num > -(self.MIN + digit) // 10:
                return False
            elif not negative and num > (self.MAX - digit) // 10:
                return False
            return True
        
        x = abs(x)
        ret = 0
        while x > 0:
            digit = x % 10
            if not check(ret, digit):
                return 0
            ret = ret * 10 + digit
            x = x // 10
        
        return -ret if negative else ret
