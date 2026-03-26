class Solution:
    def isValid(self, s: str) -> bool:
        par = {}
        par[')'] = '('
        par[']'] = '['
        par['}'] = '{'

        stack = []
        left = ['(', '[', '{']
        for ele in s:
            if ele in left:
                stack.append(ele)
            else:
                if not stack or stack[-1] != par[ele]:
                    return False
                stack.pop()

        return len(stack) == 0
       


