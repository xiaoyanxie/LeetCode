class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        "flower",
        "flow",
        "flight"
           i
        """
        def getPrefixAt(i):
            if i >= len(strs[0]):
                return None
            c = strs[0][i] # o
            for s in strs:
                if i >= len(s) or s[i] != c:
                    return None
            return c

        i = 0
        prefix = [] # fl
        while i < 200:
            p = getPrefixAt(i)
            if not p:
                break
            prefix.append(p)
            i += 1
        return ''.join(prefix)
