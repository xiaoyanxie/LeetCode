class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0
        for _ in range(32):
            if n & 1 > 0:
                cnt += 1
            n >>= 1
        return cnt
