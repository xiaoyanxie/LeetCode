from collections import defaultdict
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        """
        cdeedebbcccbdaa
                     ^
           
        stack: [(c, 1), (d, 1), (e, 1), (e, 2), (d, 1), (e, 1), (d, 1)]

        Time: O(N)
        Space: O(N)
        """

        stack = []
        for c in s:
            if stack and stack[-1][0] == c and stack[-1][1] >= k - 1:
                stack.pop()
            elif stack and stack[-1][0] == c:
                stack[-1][1] += 1
            else:
                stack.append([c, 1])
        
        return ''.join( c * freq for c, freq in stack )
