class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        ret = []

        for c in s:
            if c != ')':
                ret.append(c)
                if c == '(':
                    stack.append(len(ret) - 1)
            elif stack:
                stack.pop()
                ret.append(c)
        
        while stack:
            ret[stack.pop()] = ''

        return ''.join(ret)
