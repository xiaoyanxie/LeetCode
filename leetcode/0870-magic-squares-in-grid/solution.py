class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        """
        [7,0,5],
        [2,4,6],
        [3,8,1]
        """
        if rows < 3 or cols < 3:
            return 0
        square = [ [ [0] for j in range(3) ] for i in range(3) ]
        def isMagicSquare(di, dj):
            seen = set()
            for i in range(di, di + 3):
                for j in range(dj, dj + 3):
                    if grid[i][j] > 9: return False
                    seen.add(grid[i][j])
                    square[i - di][j - dj] = grid[i][j]
            if len(seen) != 9:
                return False

            # print(square)
            # row -> sum
            rowsSum = {
                0: sum(square[0]),
                1: sum(square[1]),
                2: sum(square[2]) 
            }
            # col -> sum
            colsSum = {
                0: sum([ square[i][0] for i in range(3) ]),
                1: sum([ square[i][1] for i in range(3) ]),
                2: sum([ square[i][1] for i in range(3) ])
            }
            # 
            diagnalSum = {
                0: sum([ square[0][0], square[1][1], square[2][2] ]),
                1: sum([ square[0][2], square[1][1], square[2][0] ])
            }
            # print(diagnalSum)
            cond0 = rowsSum[0] == 15
            cond1 = rowsSum[0] == rowsSum[1] and rowsSum[1] == rowsSum[2]
            cond2 = colsSum[0] == colsSum[1] and colsSum[1] == colsSum[2]
            cond3 = diagnalSum[0] == diagnalSum[1]
            cond4 = rowsSum[0] == colsSum[0] and colsSum[0] == diagnalSum[0]
            return cond0 and cond1 and cond2 and cond3 and cond4

        cnt = 0
        for di in range(rows - 2):
            for dj in range(cols - 2):
                # print(f'{di}, {dj}')
                if isMagicSquare(di, dj): cnt += 1
        
        return cnt
