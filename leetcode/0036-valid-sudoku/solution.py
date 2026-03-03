from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        rows = { i: set() for i in range(n) }
        cols = { i: set() for i in range(n) }
        boxes = { i: set() for i in range(1, 10) }

        def getBoxId(i, j):
            """
              0 1 2 | 3 4 5 | 6 7 8
            0
            1   1       2       3
            2
            -
            3
            4   4       5       6
            5
            -
            6
            7   7       8       9
            8
            """
            if 0 <= i <= 2 and 0 <= j <= 2:
                return 1
            elif 3 <= i <= 5 and 0 <= j <= 2:
                return 2
            elif 6 <= i <= 8 and 0 <= j <= 2:
                return 3
            elif 0 <= i <= 2 and 3 <= j <= 5:
                return 4
            elif 3 <= i <= 5 and 3 <= j <= 5:
                return 5
            elif 6 <= i <= 8 and 3 <= j <= 5:
                return 6
            elif 0 <= i <= 2 and 6 <= j <= 8:
                return 7
            elif 3 <= i <= 5 and 6 <= j <= 8:
                return 8
            elif 6 <= i <= 8 and 6 <= j <= 8:
                return 9

            raise Exception('unreachable')

        """
            0   1   2 | 3   4   5 | 6   7   8
        0[["5","3",".",".","7",".",".",".","."]
        1,["6",".",".","1","9","5",".",".","."]
        2,[".","9","8",".",".",".",".","6","."]
        _   0   1   2 | 3   4   5 | 6   7   8
        3,["8",".",".",".","6",".",".",".","3"]
        4,["4",".",".","8",".","3",".",".","1"]
        5,["7",".",".",".","2",".",".",".","6"]
        _   0   1   2 | 3   4   5 | 6   7   8
        6,[".","6",".",".",".",".","2","8","."]
        7,[".",".",".","4","1","9",".",".","5"]
        8,[".",".",".",".","8",".",".","7","9"]]

        rows: 
        0: 5, 3, 7
        1: 6, 1, 9, 5
        2: 9, 9

        cols:
        0: 5, 6
        1: 3, 9
        2: 9
        3: 1
        4: 7, 9
        5: 5

        boxes:

        """

        for i in range(n):
            for j in range(n):
                if board[i][j] == '.':
                    continue

                # assert 1 <= int(board[i][j]) <= 9
                
                if board[i][j] in rows[i]:
                    return False
                rows[i].add(board[i][j])

                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
                
                boxId = getBoxId(i, j)
                if board[i][j] in boxes[boxId]:
                    return False
                boxes[boxId].add(board[i][j])

        return True
