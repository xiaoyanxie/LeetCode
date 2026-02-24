class Solution:
    def romanToInt(self, s: str) -> int:
        """
        LIX - 59

        DXC - 590
        """
        roman2int = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        ret = 0

        for i, roman in enumerate(s):
            nxt_roman = s[i + 1] if i + 1 < len(s) else None
            if nxt_roman and roman2int[roman] < roman2int[nxt_roman]:
                ret -= roman2int[roman]
            else:
                ret += roman2int[roman]

        return ret
