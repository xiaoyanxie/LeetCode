class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        table = collections.defaultdict(int)
        for ele in s:
            table[ele] += 1
        
        for ele in t:
            if ele not in table:
                return False
            elif table[ele] == 0:
                return False
            table[ele] -= 1
        
        for value in table.values():
            if value != 0:
                return False
            
        return True
 
