class Solution:
    def calculate(self, s: str) -> int:
        """
        +3 +2 /1 *2 +
                    ^


        """
        s += '+'
        stack = [] # +3 +4
        curr = 0 # 0
        op = '+' # +

        for c in s:
            if c.isdigit():
               curr = curr * 10 + int(c)
            elif c in '+-*/':
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '*':
                    stack.append(stack.pop() * curr)
                else:
                    stack.append(int(stack.pop() / curr))
                
                curr = 0
                op = c
        
        return sum(stack)
