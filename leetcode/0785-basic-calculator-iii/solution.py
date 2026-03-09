class Solution:
    def calculate(self, s: str) -> int:
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
            elif c == '(':
                stack.append(op)
                op = '+'
            elif c == ')':
                while stack:
                    p = stack.pop()
                    if type(p) == int:
                        if op == '+':
                            num = p + num
                        elif op == '-':
                            num = p - num
                        elif op == '*':
                            num = p * num
                        else:
                            num = int(p / num)
                        
                        op = '+'
                    elif p in '+-*/':
                        op = p
                        break
                    else:
                        raise Exception(f'unexpected element on stack {p}')
            else:
                raise Exception(f'unexpected character {c}')
        return sum(stack)
