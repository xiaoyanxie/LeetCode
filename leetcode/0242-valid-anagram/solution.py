from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mp = defaultdict(int)
        for c in s:
            mp[c] += 1
        
        for c in t:
            if c not in mp:
                return False
            mp[c] -= 1
            if mp[c] == 0:
                del mp[c]
        
        return len(mp) == 0
