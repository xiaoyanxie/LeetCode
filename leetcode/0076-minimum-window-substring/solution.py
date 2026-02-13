from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        freqs = defaultdict(int)
        freqt = defaultdict(int)
        fullWindow = False
        best = None

        for c in t: 
            freqt[c] += 1
        
        def isFullWindow():
            for c in freqt:
                if freqs[c] < freqt[c]:
                    return False
            return True

        for r, c in enumerate(s):
            if c not in freqt:
                continue
            
            freqs[c] += 1
            if not fullWindow:
                if isFullWindow():
                    fullWindow = True
            
            if fullWindow:
                while s[l] not in freqt or freqs[s[l]] > freqt[s[l]]:
                    freqs[s[l]] -= 1
                    l += 1

                if not best or best[1] - best[0] > r - l:
                    best = (l, r)

        return s[best[0]:best[1] + 1] if best else "" 
            
