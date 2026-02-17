class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        num1 - Sum(k, lambda i: num2 - 2**i) == 0
        num1 - k * num2 == Sum(k, lambda i: 2**i)
                        == 2**i1 + 2**i2 + 2**i3 + ... + 2**ik

        let target = num1 - k * num2
        then:
            1. lower bound is k: if all the choosen i are 0, target = k
            2. upper bound is having k bits of 1s
        """

        for k in range(0, 64):
            target = num1 - k * num2
            if target < 0:
                break

            if target < k:
                continue

            if target.bit_count() <= k:
                return k
        return -1
