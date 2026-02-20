class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        # players = ['Alice', 'Bob']
        # def nextPlayer(i) -> str:
        #     return (i + 1) % 2

        # dup = set()

        # @cache
        # def sim(player, x, y) -> int:
        #     if x == 0 and y == 0:
        #         return player
        #     player = nextPlayer(player)
        #     if x == 0:
        #         return sim(player, x, y - 1)
        #     if y == 0:
        #         return sim(player, x - 1, y)
        #     else:
        #         return sim(player, x - 1, y) or sim(player, x, y - 1)
        
        # ways = 0
        # for x in range(1, m + 1):
        #     for y in range(1, n + 1):
        #         # if sim(-1, x, y):
        #             # ways += 1
        #         if (x + y) % 2 != 0:
        #             ways += 1
        # return ways

        def odd(n):
            return (n + 1) // 2
        def even(n):
            return n // 2
        
        return odd(n) * even(m) + odd(m) * even(n)

