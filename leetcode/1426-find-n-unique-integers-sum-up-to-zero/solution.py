class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        ret = [] # [0, 1, -1, 2, -2]
        if n % 2 != 0:
            ret.append(0)
        
        for num in range(1, (n // 2) + 1):
            ret.append(num)
            ret.append(-num)

        return ret
