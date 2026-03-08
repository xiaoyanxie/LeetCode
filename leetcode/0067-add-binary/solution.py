class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
        1011
           i
        """
        i = 0
        ret = 0
        while i < len(a) or i < len(b):
            ai = int(a[len(a) - i - 1]) if i < len(a) else 0
            bi = int(b[len(b) - i - 1]) if i < len(b) else 0

            factor = 2**i
            ret += ai * factor + bi * factor
            i += 1
        
        return bin(ret)[2:]
