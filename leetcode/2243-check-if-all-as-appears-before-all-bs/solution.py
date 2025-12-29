class Solution:
    def checkString(self, s: str) -> bool:
        if len(s) == 1:
            return True
        # count = 1
        for i in range(1, len(s)):
            if s[i] != s[i - 1]:
                if s[i] != 'b' or s[i - 1] != 'a':
                    # print(i,s[i], s[i-1])
                    return False
                # count += 1
        
        return True
                
