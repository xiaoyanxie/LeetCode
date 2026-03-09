class Solution:
    def checkValidString(self, s: str) -> bool:
        lparens = []
        stars = []

        for i, c in enumerate(s):
            if c == '(':
                lparens.append(i)
            elif c == '*':
                stars.append(i)
            else:
                assert c == ')'
                if lparens:
                    lparens.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            
        while lparens:
            if stars and lparens.pop() < stars.pop():
                continue
            return False
        return True
