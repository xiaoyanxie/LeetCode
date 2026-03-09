class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        """
                    1 < x <= n
        Alice                       Bob
                    1 < y <= m
        
        
        Alice wins if x + y is odd

        (x + y) % 2 != 0

        1, 2, 3, 4
        1, 2, 3, 4

        1, 2, 3
        1, 2, 3, 4, 5, 6

        if n == m:
            return (n - 2) * 2 + 2
        
        x = max(n, m)
        return (x - 1) * 2 + 1

        (1, 2), (2, 1), (2, 3), (3, 2), (4, 3)
        """
        def odds(x):
            return math.ceil(x / 2)
        
        def evens(x):
            return x // 2
        
        return odds(m) * evens(n) + evens(m) * odds(n)
