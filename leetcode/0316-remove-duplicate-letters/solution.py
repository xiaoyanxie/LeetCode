class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        cbacdcbc
                ^
        acdb

        cbaxycbxy
                ^
        stack: a,c,b,x,y
        seen: {a,c,b,x,y}
        freq: {c:0, b:0, a:0, x:0, y:0}

        bcabc
            ^
        abc
        """
        stack = []
        seen = set()
        freq = Counter(s)
        for c in s:
            freq[c] -= 1

            if c in seen:
                continue
            
            while stack and c < stack[-1] and freq[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(c)
            seen.add(c)
        
        return ''.join(stack)
