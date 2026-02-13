class Solution:
    #left but no rihgt
    #right but no left
    #first right then left
    #first right then left

    def minRemoveToMakeValid(self, s: str) -> str:
        left = 0
        right = 0
        remove =set()
        for i, letter in enumerate(s):
            if letter == ")":
                right += 1
                if right > left:
                    remove.add(i)
                    right -= 1
            elif letter == "(":
                left += 1
   
        if left != right:
        #     if right == 0:
        #         return ""
    
            more = left - right
            
            for i, letter in enumerate(s[::-1]):
                if more == 0:
                    break
                if letter == "(":
                    remove.add(len(s) - i - 1)
                    more -= 1
        res = []
        for i, letter in enumerate(s):
            if i not in remove:
                res.append(letter)
            
        return ''.join(res)
            
