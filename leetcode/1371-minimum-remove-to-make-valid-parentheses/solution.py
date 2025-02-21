class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        #First remove unpaired ')'
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            elif s[i] == ")":
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        #Second remove unpaired '('
        while stack:
            s[stack.pop()] = ''
        
        return ''.join(s)
        # #change my original solution to helper function to reduce the space 
        # def delete_invalid_paren(s, open_symbol, close_symbol):
        #     count = 0
        #     result = []
        #     for char in s:
        #         if char == open_symbol:
        #             count += 1
        #         elif char == close_symbol:
        #             if count == 0:
        #                 continue
        #             else:
        #                 count -= 1
        #         result.append(char)
            
        #     return "".join(result)
            
        # s = delete_invalid_paren(s, "(", ")")
        # s = delete_invalid_paren(s[::-1], ")", "(")
        # return s[::-1]

        

#below is my original method with two list which has good runtime yet bad space.
        # count = 0
        # result = []

        # for alpha in s:
        #     if alpha == "(":
        #         count+=1
        #     elif alpha == ")":
        #         if count == 0:
        #             continue
        #         count-=1
        #     result.append(alpha)

        # update = []
        # openNeeded = count

        # for alpha in reversed(result):
        #     if alpha == "(" and openNeeded > 0:
        #         openNeeded -=1
        #         continue
        #     update.append(alpha)

        # return "".join(reversed(update))
