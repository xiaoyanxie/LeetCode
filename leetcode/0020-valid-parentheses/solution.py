class Solution:
    def isValid(self, s: str) -> bool:
        mp = {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        for p in s:
            if p in mp:
                stack.append(p)
            elif len(stack) == 0:
                return False
            elif mp[stack.pop()] != p:
                return False
        return len(stack) == 0
