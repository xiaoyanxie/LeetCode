class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        n = len(board[0])

        def crash() -> bool:
            stable = True
            for i in range(m):
                for j in range(n - 2):
                    v1, v2, v3 = abs(board[i][j]), abs(board[i][j + 1]), abs(board[i][j + 2])
                    if v1 != 0 and v1 == v2 == v3:
                        board[i][j] = board[i][j + 1] = board[i][j + 2] = -v1
                        stable = False
        
            for j in range(n):
                for i in range(m - 2):
                    v1, v2, v3 = abs(board[i][j]), abs(board[i + 1][j]), abs(board[i + 2][j])
                    if v1 != 0 and v1 == v2 == v3:
                        board[i][j] = board[i + 1][j] = board[i + 2][j] = -v1
                        stable = False
                    
            if not stable:
                for i in range(m):
                    for j in range(n):
                        if board[i][j] < 0:
                            board[i][j] = 0
            return stable

        def drop(j):
            """t
            0  
            0   
            0  
            0 b
            1 
            3  
            2
            1  
            """
            t = m - 1
            while t >= 0 and board[t][j] != 0:
                t -= 1
            
            b = t
            while t >= 0:
                if board[t][j] != 0:
                    board[b][j], board[t][j] = board[t][j], board[b][j]
                    b -= 1
                t -= 1
        
        stable = False
        while not stable:
            stable = crash()
            if stable: break
            for j in range(n):
                drop(j)
        return board

