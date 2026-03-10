class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        """
        cbacdcbc

        cdacdcbc
                ^
        acdb
        
        seen: set
        stack
        freq: hashmap

        1. while s[i] not in seen and s[i] < acc[-1] and acc[-1] has duplicates
            then remove acc[-1]
        2. concat s[i]

        freq: {c:0, d:0, a:0, b:0}
        stack: acdb
        seen: acdb
        cdacdcbc
                ^
        """

        seen = set()
        stack = []
        freq = Counter(s)

        for c in s:
            freq[c] -= 1

            if c in seen:
                continue

            while stack and c < stack[-1] and freq[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(c)
            seen.add(c)
        
        # print(f'freq={freq}, stack={stack}')
        return ''.join(stack)
