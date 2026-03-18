class Solution:
    def decodeString(self, s: str) -> str:
        """
        3[a]2[bc]

        3[a2[c2[b]2[b]]]
                  c
        k = 0
        acc = [cbb]
        stack: 3, a, 2, 

        2[a2[c]bc]3[cd]ef
         ^

        k = 2

        

        [21 * accbc, ]
         cdcdcdef

        3[a2[c2[b]2[b]]]
                       i
        stack:  
        acc: acbbbbcbbbb acbbbbcbbbb acbbbbcbbbb
        k: 0

        3[a]2[bc]
           c
        stack: aaa
        acc: bcbc
        k: 0

        3[a2[c]]3[a]a
                   ^

        stack: ([accaccacc], 3)
        k: 0
        acc: [a]
        """
        stack = []
        acc = []
        k = 0
        for c in s:
            if c.isdigit():
                k = k * 10 + int(c)
            elif 'a' <= c <= 'z':
                assert k == 0
                acc.append(c)
            elif c == '[':
                assert k > 0
                stack.append((acc, k))
                k = 0
                acc = []
            elif c == ']':
                prevAcc, prevK = stack.pop()
                acc = prevAcc + prevK * acc
    
        return ''.join(acc)
