class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minLen = min([ len(s) for s in strs ])
    
        def prefixAt(i):
            prefixi = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != prefixi:
                    return None
            return prefixi

        ret = ''
        for i in range(minLen):
            prefixi = prefixAt(i)
            if not prefixi:
                break
            ret += prefixi
        
        return ret
