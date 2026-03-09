class Solution:
    def concatenatedBinary(self, n: int) -> int:
        """
        n.bit_length()

        101

        digit: 100

        ret = 0
        while n > 0:
            digit = n % 10
            n //= 10
            ret = (digit << ret.bit_length()) | ret

        1, 2, 3

        ret: 11011
             43210
        16 + 8 + 2 + 1
        """
        ret = 0
        for i in range(1, n + 1):
            ret = ((ret << i.bit_length()) | i) % (10**9 + 7)
        
        return ret
