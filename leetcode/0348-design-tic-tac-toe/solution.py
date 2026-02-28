from collections import defaultdict
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        # player -> #row -> count
        self.rows = { 1: defaultdict(int), 2: defaultdict(int) }
        # player -> #col -> count
        self.cols = { 1: defaultdict(int), 2: defaultdict(int) }
        # player -> #diagonal (1 / 2) -> count
        self.diagonals = { 1: defaultdict(int), 2: defaultdict(int) }

    def move(self, row: int, col: int, player: int) -> int:
        """
         0,1,2
        0
        1
        2
        """
        self.rows[player][row] += 1
        if self.rows[player][row] == self.n:
            return player

        self.cols[player][col] += 1
        if self.cols[player][col] == self.n:
            return player

        if row == col:
            self.diagonals[player][1] += 1
            if self.diagonals[player][1] == self.n:
                return player

        if row == self.n - col - 1:
            self.diagonals[player][2] += 1
            if self.diagonals[player][2] == self.n:
                return player
        
        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
