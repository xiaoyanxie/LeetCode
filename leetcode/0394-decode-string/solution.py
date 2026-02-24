class Solution:
    def decodeString(self, s: str) -> str:
        # 3[a2[c]]
        stack = [] # [ ]
        currNum = 0 # 
        currStr = '' # accaccacc
        for i, c in enumerate(s):
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            elif ord('a') <= ord(c) <= ord('z'):
                currStr += c
            elif c == '[':
                stack.append((currStr, currNum))
                currStr = ''
                currNum = 0
            elif c == ']':
                prevStr, N = stack.pop() # '', 3
                currStr = prevStr + N * currStr
            else:
                raise Exception('unreachable')

        return currStr
