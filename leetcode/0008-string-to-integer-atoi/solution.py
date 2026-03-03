class Solution:
    def myAtoi(self, s: str) -> int:
        MIN, MAX = -0x8000_0000, 0x7FFF_FFFF

        """
        s = '  '
        s = '  +'
        s = '  w'
        s = '  -w'
        s = '   -042'
        """

        acc = 0
        sign = 1
        i = 0
        while i < len(s):
            if s[i] == ' ':
                i += 1
            else:
                break

        if i == len(s) or (s[i] not in '+-' and not s[i].isdigit()):
            return acc

        if s[i] == '+': 
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1

        def add(sign, acc, digit) -> Tuple[int, bool]:
            """
            if sign == -1: 
              MIN <= acc * 10 - digit
              (MIN + digit) / 10 <= acc

            else:
               acc * 10 + digit <= MAX
               acc <= (MAX - digit) / 10
            """
            if sign == -1:
                if (MIN + digit) / 10 <= acc:
                    return acc * 10 - digit, False
                else:
                    return MIN, True
            else:
                if acc <= (MAX - digit) / 10:
                    return acc * 10 + digit, False
                else:
                    return MAX, True

        while i < len(s):
            c = s[i]
            if not c.isdigit():
                break
            
            acc, overflow = add(sign, acc, int(c))
            if overflow:
                break
            i += 1
        return acc
