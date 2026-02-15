class Solution:
    def findPermutation(self, s: str) -> List[int]:
        i = 0
        res = list(range(1, len(s) + 2))
        start = 0
        while i < len(s):
            if s[i] == "D":
                start = i
                while i < len(s) and s[i] =="D":
                    i+=1
                res[start:i+1] = res[start:i+1][::-1]
            else:
                i+=1
        
        return res
