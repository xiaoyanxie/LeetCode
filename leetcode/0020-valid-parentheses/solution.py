class Solution:
    def isValid(self, s: str) -> bool:
        res = []
       
        open = ["(","[","{"]
        close = [")","]","}"]
        for p in s:
            if p in open:
                res.append(p)
            else:
                if (not res) or (open.index(res[-1]) != close.index(p)):
                    return False
                else:
                    res.pop()
        
        return not res
        # for p in s:
        #     if p in "[{(":
        #         res.append(p)
        #     elif p in "]})":
        #         if not res:
        #             return False
        #         if p == "]" and res[-1] =="[":
        #             res.pop()
        #         elif p == ")" and res[-1] =="(":
        #             res.pop()
        #         elif p == "}" and res[-1] =="{":
        #             res.pop()
        #         else:
        #             return False
                
        # return len(res)==0
