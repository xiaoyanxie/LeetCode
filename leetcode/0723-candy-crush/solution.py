class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        cols = len(board[0])
        vertical = [ (1, 0), (-1, 0) ]
        horizontal = [ (0, 1), (0, -1) ]

        def isValidLoc(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def detectCrash(i, j, direction, candidates):
            potentials = []
            if direction == vertical:
                for ni in reversed(range(i - 2, i)):
                    if not isValidLoc(ni, j) or board[ni][j] != board[i][j]:
                        break
                    potentials.append((ni, j))
                for ni in range(i, i + 2):
                    if not isValidLoc(ni, j) or board[ni][j] != board[i][j]:
                        break
                    potentials.append((ni, j))
            else:
                for nj in reversed(range(j - 2, j)):
                    if not isValidLoc(i, nj) or board[i][nj] != board[i][j]:
                        break
                    potentials.append((i, nj))
                for nj in range(j, j + 2):
                    if not isValidLoc(i, nj) or board[i][nj] != board[i][j]:
                        break
                    potentials.append((i, nj))

            if len(potentials) >= 3:
                for ni, nj in potentials:
                    candidates.add((ni, nj))

        # def crash(candidates):
        #     for i, j in candidates:
        #         board[i][j] = 0

        def gravityPull(j):
            tmp = [ board[i][j] for i in range(rows) if board[i][j] != 0 ]
            if len(tmp) == rows:
                return
            
            zeros = rows - len(tmp)
            for i in range(0, zeros):
                board[i][j] = 0
            for i in range(zeros, rows):
                board[i][j] = tmp[i - zeros]

        while True:
            # scan the board 
            candidates = set()
            for i in range(rows):
                for j in range(cols):
                    if board[i][j] == 0:
                        continue
                    detectCrash(i, j, vertical, candidates)
                    detectCrash(i, j, horizontal, candidates)
            
            if not candidates:
                break

            for i, j in candidates:
                board[i][j] = 0
            
            for j in range(cols):
                gravityPull(j)
        return board
