class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        directions = [ (0, 1), (0, -1), (1, 0), (-1, 0) ]

        def isValidLoc(i, j):
            return 0 <= i < rows and 0 <= j < cols

        def match(i, j, wi):
            if wi == len(word):
                return True
            if board[i][j] != word[wi]:
                return False
            if wi == len(word) - 1:
                return True

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if not isValidLoc(ni, nj) or board[ni][nj] == '':
                    continue
                tmp, board[i][j] = board[i][j], ''
                if match(ni, nj, wi + 1):
                    return True
                board[i][j] = tmp
            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] != word[0]:
                    continue
                if match(i, j, 0):
                    return True
        return False
