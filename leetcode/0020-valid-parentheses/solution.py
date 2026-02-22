class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {
         ')': '(',
         ']': '[',
         '}': '{'
        }
        for c in s:
            if c not in mp:
                stack.append(c)
            elif not stack or mp[c] != stack[-1]:
                return False
            else:
                stack.pop()

        return len(stack) == 0
