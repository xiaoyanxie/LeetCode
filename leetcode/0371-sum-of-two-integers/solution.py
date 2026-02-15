class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0: return b
        if b == 0: return a
        mask = 0xFFFFFFFF
        sign = 0b1000_0000_0000_0000_0000_0000_0000_0000
        while b != 0:
            xor = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            a = xor
            b = carry
        
        if a & sign > 0: 
            return ~(a ^ mask)
        return a

