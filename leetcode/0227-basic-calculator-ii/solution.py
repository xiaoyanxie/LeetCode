class Solution:
    def calculate(self, s: str) -> int:
        """
        [+3, -4, +2]

        +3 -2 *2 /1 +2 +
                       ^
        """

        s += '+'
        stack = []
        op = '+'
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in '+-*/':
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                op = c
                num = 0
        return sum(stack)
