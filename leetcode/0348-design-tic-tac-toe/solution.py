class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.verticalMoves = {
            1: defaultdict(int), 2: defaultdict(int)
        }
        self.horizontalMoves = {
            1: defaultdict(int), 2: defaultdict(int)
        }
        self.diagonalMoves = {
            1: defaultdict(int), 2: defaultdict(int)
        }
        """
        verticalMoves: {
            1: {0:2, 1:1, 2:1}
            2: {0:1, 1:1, 2:1}
        }
        horizontalMoves: {
            1: {0:1, 2:3}
            2: {0:1, 1:2}
        }
        diagonalMoves: {
            1: {0:1, 1:2}
            2: {0:2, 1:1}
        }
        22 . 1
        1. . .
        01 . .
         0 1 2
        """

    def move(self, row: int, col: int, player: int) -> int:
        self.verticalMoves[player][col]+=1
        if self.verticalMoves[player][col] == self.n:
            return player
        
        self.horizontalMoves[player][row] += 1
        if self.horizontalMoves[player][row] == self.n:
            return player
        
        if row == col and self.n % 2 == 1 and row == self.n // 2:
            self.diagonalMoves[player][0] += 1
            self.diagonalMoves[player][1] += 1
        elif row == col:
            self.diagonalMoves[player][1] += 1
        elif row == self.n - col - 1:
            self.diagonalMoves[player][0] += 1

        return player if self.diagonalMoves[player][0] == self.n or self.diagonalMoves[player][1] == self.n else 0
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
