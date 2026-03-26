class Codec:
    def encode(self, strs: List[str]) -> str:
        res = list()
        for s in strs:
            n = len(s)
            res.append(str(n))
            res.append("#")
            res.append(s)
        return "".join(res)
        

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            l = int(s[i:j])
            res.append(s[j+1:j+1+l])            
            i = j + 1 + l
        
        return res
"""
5#Hello5#World
^
      i
 j
  l    l
"""

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
