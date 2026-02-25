class Solution:
    def sumZero(self, n: int) -> List[int]:
        ret = []
        
        if n % 2 != 0:
            ret.append(0)
            half = (n - 1) // 2
        else:
            half = n // 2
        
        for n in range(1, half + 1):
            ret.append(n)
            ret.append(-n)
        
        return ret
