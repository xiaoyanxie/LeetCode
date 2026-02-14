class Solution:
    def countBits(self, n: int) -> List[int]:
        """
        0 - 0b0
        1 - 0b1
        2 - 0b10
        3 - 0b11
        4 - 0b100
        5 - 0b101
        6 - 0b110
        7 - 0b111
        8 - 0b1000
        9 - 0b1001
        10- 0b1010
        11- 0b1011
        """
        ans = [0] * (n + 1)
        for i in range(n + 1):
            ans[i] = ans[i >> 1] + (i & 0b1)
        return ans
