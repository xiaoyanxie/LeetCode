class Solution:
    def numOfWays(self, n: int) -> int:
        """
        r y r
        (y r y, y g y, g r g), (g r y, y r g)
        g r y
        (r g r, r y r), (r y g, y g r)
        """
        type2 = 6
        type3 = 6

        for i in range(2, n + 1):
            type2, type3 = 3 * type2 + 2 * type3, 2 * type2 + 2 * type3

        return (type2 + type3) % (10**9 + 7)

    def bruteforce(self, n):
        grid = [ [-1,-1,-1] for _ in range(n) ]

        colors = set((0, 1, 2))

        def paint(i, j):
            if i == n or j == 3:
                return 0
            top = grid[i - 1][j] if i > 0 else -1
            left = grid[i][j - 1] if j > 0 else -1
            available = colors - { top, left }
            if i == n - 1 and j == 2:
                return len(available)
            ways = 0
            for color in available:
                grid[i][j] = color
                if i + 1 < n:
                    ways += paint(i + 1, j)
                else:
                    ways += paint(0, j + 1)
                grid[i][j] = -1
            return ways

        return paint(0, 0) % (10**9 + 7)
