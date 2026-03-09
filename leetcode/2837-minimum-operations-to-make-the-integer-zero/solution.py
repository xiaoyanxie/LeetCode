class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        num1 - k * (2^i + num2) = 0

        num1 - k * num2 = k sum 2^i

        seach a k to make:
            (num1 - k * num2) to be at least k
            and
            (num1 - k * num2).bit_count() in (0, k]
        """

        for k in range(0, 60):
            x = num1 - k * num2
            if k <= x and 0 < x.bit_count() <= k:
                return k
        
        return -1
