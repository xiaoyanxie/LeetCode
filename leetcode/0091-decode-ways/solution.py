class Solution:
    def numDecodings(self, s: str) -> int:
        """
        code book:
        1  - A
        2  - B
        3  - C
        4  - D
        ...
        26 - Z

        1 2 4 2 1
        1 2 3 3 4

        2 2 6
        1 2 3

        1 6 0 7
        1 2 0
        """

        @cache
        def dfs(i) -> int:
            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i == len(s) - 1:
                return 1
            
            ways = 0
            ways += dfs(i + 1)
            if 1 <= int(f'{s[i]}{s[i + 1]}') <= 26:
                ways += dfs(i + 2)
            return ways

        return dfs(0)
        

