class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """
        a)b(c)d
               ^

        ))((
           ^

        lee(t(c)o)de)
                    ^
        lparens: 
        rparens: 12


        a)(b(c)d
               ^
        lparens: 2
        a(b(c)d
        """

        lparens = []
        ret = list(s)
        for i, c in enumerate(ret):
            if c == '(':
                lparens.append(i)
            elif c == ')' and lparens:
                lparens.pop()
            elif c == ')':
                ret[i] = ''
        
        for i in lparens:
            ret[i] = ''

        return ''.join(ret)
