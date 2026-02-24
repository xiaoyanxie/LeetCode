class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        # player -> row -> cnt
        self.rows = {1: defaultdict(int), 2: defaultdict(int)} # {1 -> 0 -> 1, 2 -> 1 -> 1, 1 -> 2 -> 1, 2 -> 0 -> 1}
        # player -> col -> cnt
        self.cols = {1: defaultdict(int), 2: defaultdict(int)} # {1 -> 0 -> 1, 2 -> 1 -> 1, 1 -> 2 -> 1, 2 -> 2 -> 1}
        # player -> 0/1 -> cnt
        self.diagnals = {1: {0: 0, 1: 0}, 2: {0: 0, 1: 0}} # {1 -> 0 -> 2, 2 -> 0 -> 1}
        """
          0 1 2 3 4
        0     x
        1   x y
        2 x
        3
        4

          1 2
        1 2 1
        2   2

          0 1 2
        0 1   2
        1   2
        2     1
        """

    def move(self, row: int, col: int, player: int) -> int:
        self.rows[player][row] += 1
        if self.rows[player][row] == self.n:
            return player

        self.cols[player][col] += 1
        if self.cols[player][col] == self.n:
            return player

        if row == col:
            self.diagnals[player][0] += 1
            if self.diagnals[player][0] == self.n:
                return player
        if row == self.n - col - 1:
            self.diagnals[player][1] += 1
            if self.diagnals[player][1] == self.n:
                return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
