from collections import deque
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        ['(', 1], ['((', 2], ['(((', 3]

        '('
        """

        ret = []
        def dfs(l, r, acc):
            if l < n:
                assert r <= l
            if l == n and r == n:
                ret.append(acc)
            if l < n:
                dfs(l + 1, r, acc + '(')
            if r < l:
                dfs(l, r + 1, acc + ')')

        dfs(0, 0, '')
        return ret
