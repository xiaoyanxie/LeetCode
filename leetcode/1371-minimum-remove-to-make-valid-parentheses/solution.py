class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        lee(t(c)o)de)
                    ^

        ret: lee(t(c)o)de
        stack: []

        ())a((
             ^

        ret: ()a  
        stack: [3,4]
        """

        # Pass 1:
        stack = []
        ret = []
        for c in s:
            if c != ')':
                ret.append(c)
                if c == '(':
                    stack.append(len(ret) - 1)
            elif stack:
                ret.append(c)
                stack.pop()
        
        # Pass 2:
        for i in stack:
            ret[i] = ''
        
        return ''.join(ret)
